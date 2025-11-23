# 🎓 Student Introduction Scorer - Nirmaan AI Case Study

An AI-powered tool to analyze and score students' spoken communication skills from self-introduction transcripts. This application combines **rule-based methods**, **NLP-based semantic scoring**, and **data-driven rubric evaluation** to provide comprehensive feedback.

## 🌟 Project Overview

This project was developed as part of the Nirmaan AI Internship Case Study. It evaluates student self-introductions across multiple criteria:

- **Personal Introduction** - Name, age, class, school
- **Family Description** - Family members and size
- **Personal Characteristics** - Special traits and qualities
- **Hobbies and Interests** - Activities and sports
- **Fun Facts or Secrets** - Personal stories
- **Academic Interests** - Favorite subjects with reasoning
- **Structure and Coherence** - Clear beginning, middle, and end

## 🏗️ Architecture & Scoring Formula

### Three-Layered Scoring Approach

1. **Rule-Based Scoring (50% weight)**
   - Keyword matching against predefined keywords
   - Word count validation (min/max limits)
   - Formula: `(keyword_match * 0.7) + (length_compliance * 0.3)`

2. **NLP Semantic Scoring (50% weight)**
   - Uses `sentence-transformers` (all-MiniLM-L6-v2 model)
   - Calculates cosine similarity between transcript and criterion template
   - Captures semantic meaning beyond keywords

3. **Weighted Aggregation**
   - Each criterion has a weight (totaling 100%)
   - Final formula: `Σ(criterion_score * weight) / total_weight`
   - Output: Overall score from 0-100

### Example Calculation
```
For "Personal Introduction" (weight: 20%):
- Rule-based score: 85/100
- Semantic score: 78/100
- Combined: (85 * 0.5) + (78 * 0.5) = 81.5/100
- Weighted contribution: 81.5 * 20 = 16.3

Overall Score = Sum of all weighted contributions
```

## 🚀 Features

✅ **Web-based UI** - Simple, intuitive interface  
✅ **REST API** - JSON endpoint for programmatic access  
✅ **Real-time Analysis** - Instant scoring with detailed feedback  
✅ **Per-Criterion Breakdown** - Individual scores for each rubric item  
✅ **Keyword Detection** - Shows which keywords were found  
✅ **Export Functionality** - Download results as JSON  
✅ **Sample Transcript** - Pre-loaded example for testing  

## 📁 Project Structure

```
transcript-scorer/
│
├── app.py                 # Flask REST API server
├── scorer.py              # Core scoring engine (AI logic)
├── rubric.py             # Rubric configuration & criteria
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── README.md             # This file
│
├── templates/
│   └── index.html        # Frontend UI
│
└── static/
    ├── script.js         # JavaScript logic
    └── style.css         # Styling
```

## 🔧 Technology Stack

**Backend:**
- Python 3.8+
- Flask (Web framework)
- sentence-transformers (NLP model)
- scikit-learn (Utilities)
- NumPy (Numerical operations)

**Frontend:**
- HTML5
- CSS3 (Responsive design)
- Vanilla JavaScript (No frameworks)

**AI/ML:**
- Sentence-BERT model: `all-MiniLM-L6-v2`
- Cosine similarity for semantic matching

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for downloading AI models on first run)

### Step 1: Clone or Download the Project
```powershell
cd d:\nirmaan\transcript-scorer
```

### Step 2: Create Virtual Environment (Recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

**Note:** First installation will download the AI model (~80MB). This is a one-time process.

### Step 4: Run the Application
```powershell
python app.py
```

You should see:
```
Loading sentence transformer model...
Scorer initialized successfully!

============================================================
Server is ready!
Open your browser and go to: http://localhost:5000
============================================================
```

### Step 5: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 💻 Usage Guide

### Web Interface

1. **Enter Transcript**: Paste student's introduction in the text area
2. **Click "Score Transcript"**: Analyzes the text using AI
3. **View Results**: See overall score and detailed breakdown
4. **Export**: Download results as JSON for records

### Using the Sample

Click **"Load Sample"** to test with Muskan's introduction (pre-loaded).

### API Endpoint

**POST** `/api/score`

**Request:**
```json
{
  "transcript": "Hello everyone, myself Muskan..."
}
```

**Response:**
```json
{
  "overall_score": 78.5,
  "total_words": 92,
  "criteria_scores": [
    {
      "criterion": "Personal Introduction",
      "score": 85.2,
      "rule_score": 87.0,
      "semantic_score": 83.4,
      "keywords_found": ["myself", "age", "class", "school"],
      "feedback": "Excellent coverage of personal introduction!..."
    }
  ]
}
```

## 🌐 Deployment Options

### Option 1: Local Machine (Current Setup)
Already configured! Just run `python app.py`

### Option 2: AWS Free Tier
1. Launch EC2 t2.micro instance (Ubuntu)
2. Install Python 3.8+
3. Clone repository
4. Install dependencies
5. Run with: `python app.py --host 0.0.0.0 --port 80`
6. Configure security group to allow port 80

### Option 3: Heroku (Free Tier)
1. Create `Procfile`: `web: python app.py`
2. Push to Heroku Git
3. Heroku will auto-detect Python and install dependencies

### Option 4: Replit / PythonAnywhere
Upload files and run `app.py` directly in the cloud IDE.

## 📊 Sample Output

For the provided sample transcript (Muskan's introduction):

```
Overall Score: 78.5/100 ⭐
Total Words: 92

Breakdown:
- Personal Introduction: 92/100 ✓
- Family Description: 85/100 ✓
- Personal Characteristics: 78/100 ✓
- Hobbies and Interests: 82/100 ✓
- Fun Facts or Secrets: 70/100 ✓
- Academic Interests: 88/100 ✓
- Structure and Coherence: 75/100 ✓
```

## 🧪 Testing

Run the application and test with these scenarios:

1. **Full Introduction** - Use the sample (should score 75-85)
2. **Minimal Introduction** - Just name and age (should score 20-40)
3. **Empty Text** - Should show error message
4. **Long Text** - 300+ words (test performance)

## 🔍 Rubric Details

| Criterion | Weight | Min Words | Max Words |
|-----------|--------|-----------|-----------|
| Personal Introduction | 20% | 10 | 50 |
| Family Description | 15% | 5 | 40 |
| Personal Characteristics | 15% | 5 | 40 |
| Hobbies and Interests | 15% | 5 | 40 |
| Fun Facts or Secrets | 10% | 5 | 40 |
| Academic Interests | 15% | 5 | 50 |
| Structure and Coherence | 10% | 30 | 200 |

## 🤝 Contributing

This is a case study project. Suggestions welcome!

## 📝 License

Educational project for Nirmaan AI Internship Case Study.

## 👤 Author

**Your Name**  
Nirmaan AI Intern Candidate

## 🙏 Acknowledgments

- Nirmaan Education for the case study opportunity
- Sentence-Transformers library by UKPLab
- Flask framework team

---

**Questions?** Contact: [your-email@example.com]

**GitHub Repository:** [Your GitHub Link]

**Deployed App:** [Your Deployment Link]
