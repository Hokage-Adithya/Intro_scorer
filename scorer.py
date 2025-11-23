


"""
Core scoring engine combining rule-based, NLP-based, and rubric-driven approaches.
"""

import re
try:
    from sentence_transformers import SentenceTransformer, util
    import numpy as np
    NLP_AVAILABLE = True
except ImportError:
    NLP_AVAILABLE = False
    print("Warning: sentence-transformers not available. Using rule-based scoring only.")

from rubric import get_rubric, get_total_weight


class TranscriptScorer:
    def __init__(self):
        # Load pre-trained sentence transformer model for semantic similarity
        if NLP_AVAILABLE:
            print("Loading sentence transformer model...")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.rubric = get_rubric()
            print("Scorer initialized successfully!")
        else:
            self.model = None
            self.rubric = get_rubric()
            print("Scorer initialized in rule-based mode only.")
    
    def count_words(self, text):
        """Count words in text"""
        words = re.findall(r'\b\w+\b', text.lower())
        return len(words)
    
    def rule_based_score(self, text, criterion):
        """
        Rule-based scoring: keyword matching and word count checks
        Returns a score between 0 and 1
        """
        text_lower = text.lower()
        
        # Keyword matching score
        keywords_found = []
        for keyword in criterion['keywords']:
            if keyword.lower() in text_lower:
                keywords_found.append(keyword)
        
        keyword_score = len(keywords_found) / len(criterion['keywords']) if criterion['keywords'] else 0
        
        # Word count check
        word_count = self.count_words(text)
        min_words = criterion.get('min_words', 0)
        max_words = criterion.get('max_words', 1000)
        
        if word_count < min_words:
            length_score = word_count / min_words if min_words > 0 else 1.0
        elif word_count > max_words:
            length_score = max(0, 1 - (word_count - max_words) / max_words)
        else:
            length_score = 1.0
        
        # Combine keyword and length scores (70% keywords, 30% length)
        rule_score = (keyword_score * 0.7) + (length_score * 0.3)
        
        return rule_score, keywords_found, word_count
    
    def semantic_score(self, text, criterion):
        """
        NLP-based semantic similarity scoring
        Returns a score between 0 and 1
        """
        if not NLP_AVAILABLE or self.model is None:
            # Fallback to keyword-based approach when NLP not available
            return self.rule_based_score(text, criterion)[0]
        
        # Encode the transcript and the criterion's semantic template
        text_embedding = self.model.encode(text, convert_to_tensor=True)
        template_embedding = self.model.encode(criterion['semantic_template'], convert_to_tensor=True)
        
        # Calculate cosine similarity
        similarity = util.cos_sim(text_embedding, template_embedding).item()
        
        # Normalize to 0-1 range (cosine similarity is already -1 to 1, but typically 0 to 1)
        semantic_score = max(0, min(1, similarity))
        
        return semantic_score
    
    def compute_criterion_score(self, text, criterion):
        """
        Combine rule-based and semantic scores for a single criterion
        Returns weighted final score for the criterion
        """
        # Get rule-based score
        rule_score, keywords_found, word_count = self.rule_based_score(text, criterion)
        
        # Get semantic score
        semantic_score = self.semantic_score(text, criterion)
        
        # Combine scores (50% rule-based, 50% semantic)
        combined_score = (rule_score * 0.5) + (semantic_score * 0.5)
        
        # Apply criterion weight
        weighted_score = combined_score * criterion['weight']
        
        return {
            'criterion': criterion['criterion'],
            'score': round(combined_score * 100, 2),  # 0-100 scale
            'weighted_score': round(weighted_score, 2),
            'rule_score': round(rule_score * 100, 2),
            'semantic_score': round(semantic_score * 100, 2),
            'keywords_found': keywords_found,
            'word_count': word_count,
            'weight': criterion['weight'],
            'feedback': self.generate_feedback(criterion, combined_score, keywords_found, word_count)
        }
    
    def generate_feedback(self, criterion, score, keywords_found, word_count):
        """
        Generate textual feedback for a criterion
        """
        feedback = []
        
        # Performance feedback
        if score >= 0.8:
            feedback.append(f"Excellent coverage of {criterion['criterion'].lower()}!")
        elif score >= 0.6:
            feedback.append(f"Good attempt at {criterion['criterion'].lower()}.")
        elif score >= 0.4:
            feedback.append(f"Moderate coverage of {criterion['criterion'].lower()}.")
        else:
            feedback.append(f"Limited coverage of {criterion['criterion'].lower()}.")
        
        # Keyword feedback
        if keywords_found:
            feedback.append(f"Found keywords: {', '.join(keywords_found[:5])}.")
        else:
            feedback.append("No relevant keywords detected. Try including more specific details.")
        
        # Length feedback
        min_words = criterion.get('min_words', 0)
        max_words = criterion.get('max_words', 1000)
        
        if word_count < min_words:
            feedback.append(f"Consider adding more detail (current: {word_count} words, suggested: {min_words}+ words).")
        elif word_count > max_words:
            feedback.append(f"Content is quite lengthy (current: {word_count} words, suggested: {max_words} words max).")
        
        return " ".join(feedback)
    
    def score_transcript(self, transcript):
        """
        Main scoring function: processes entire transcript
        Returns overall score and per-criterion breakdown
        """
        if not transcript or len(transcript.strip()) == 0:
            return {
                'error': 'Transcript is empty',
                'overall_score': 0,
                'criteria_scores': []
            }
        
        total_word_count = self.count_words(transcript)
        criteria_results = []
        total_weighted_score = 0
        
        # Score each criterion
        for criterion in self.rubric:
            criterion_result = self.compute_criterion_score(transcript, criterion)
            criteria_results.append(criterion_result)
            total_weighted_score += criterion_result['weighted_score']
        
        # Calculate overall score (0-100)
        total_weight = get_total_weight()
        overall_score = round((total_weighted_score / total_weight) * 100, 2)
        
        return {
            'overall_score': overall_score,
            'total_words': total_word_count,
            'criteria_scores': criteria_results,
            'rubric_weight_total': total_weight
        }


# Singleton instance
_scorer_instance = None

def get_scorer():
    """Get or create scorer instance"""
    global _scorer_instance
    if _scorer_instance is None:
        _scorer_instance = TranscriptScorer()
    return _scorer_instance
