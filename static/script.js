// Sample transcript for testing
const SAMPLE_TRANSCRIPT = `Hello everyone, myself Muskan, studying in class 8th B section from Christ Public School. 
I am 13 years old. I live with my family. There are 3 people in my family, me, my mother and my father.
One special thing about my family is that they are very kind hearted to everyone and soft spoken. One thing I really enjoy is play, playing cricket and taking wickets.
A fun fact about me is that I see in mirror and talk by myself. One thing people don't know about me is that I once stole a toy from one of my cousin.
My favorite subject is science because it is very interesting. Through science I can explore the whole world and make the discoveries and improve the lives of others. 
Thank you for listening.`;

// Store the latest results
let latestResults = null;

// Load sample transcript
function loadSample() {
    document.getElementById('transcript').value = SAMPLE_TRANSCRIPT;
}

// Clear form
function clearForm() {
    document.getElementById('transcript').value = '';
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
}

// Score the transcript
async function scoreTranscript() {
    const transcript = document.getElementById('transcript').value.trim();
    
    // Validate input
    if (!transcript) {
        showError('Please enter a transcript to score.');
        return;
    }

    // Hide previous results and errors
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    
    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('scoreBtn').disabled = true;

    try {
        // Call API
        const response = await fetch('/api/score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ transcript })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to score transcript');
        }

        // Store results
        latestResults = data;

        // Display results
        displayResults(data);

    } catch (error) {
        showError(`Error: ${error.message}`);
    } finally {
        // Hide loading
        document.getElementById('loading').style.display = 'none';
        document.getElementById('scoreBtn').disabled = false;
    }
}

// Display results
function displayResults(data) {
    // Show results section
    document.getElementById('results').style.display = 'block';

    // Display overall score
    const overallScore = Math.round(data.overall_score);
    document.getElementById('overallScore').textContent = overallScore;
    document.getElementById('totalWords').textContent = data.total_words;

    // Score interpretation
    const interpretation = getScoreInterpretation(overallScore);
    document.getElementById('scoreInterpretation').innerHTML = `<strong>${interpretation}</strong>`;

    // Color code the overall score
    const scoreCircle = document.querySelector('.score-circle');
    if (overallScore >= 80) {
        scoreCircle.style.borderColor = '#22c55e';
        scoreCircle.style.color = '#22c55e';
    } else if (overallScore >= 60) {
        scoreCircle.style.borderColor = '#3b82f6';
        scoreCircle.style.color = '#3b82f6';
    } else if (overallScore >= 40) {
        scoreCircle.style.borderColor = '#f59e0b';
        scoreCircle.style.color = '#f59e0b';
    } else {
        scoreCircle.style.borderColor = '#ef4444';
        scoreCircle.style.color = '#ef4444';
    }

    // Display criteria breakdown
    const criteriaContainer = document.getElementById('criteriaBreakdown');
    criteriaContainer.innerHTML = '';

    data.criteria_scores.forEach(criterion => {
        const card = createCriterionCard(criterion);
        criteriaContainer.appendChild(card);
    });

    // Scroll to results
    document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
}

// Create criterion card
function createCriterionCard(criterion) {
    const card = document.createElement('div');
    card.className = 'criterion-card';

    const score = Math.round(criterion.score);
    const barColor = getScoreColor(score);

    card.innerHTML = `
        <div class="criterion-header">
            <h4>${criterion.criterion}</h4>
            <div class="criterion-score" style="color: ${barColor}">
                ${score}/100
            </div>
        </div>
        
        <div class="score-bar">
            <div class="score-bar-fill" style="width: ${score}%; background-color: ${barColor}"></div>
        </div>

        <div class="criterion-details">
            <div class="detail-row">
                <span class="label">Weight:</span>
                <span class="value">${criterion.weight}%</span>
            </div>
            <div class="detail-row">
                <span class="label">Rule-Based Score:</span>
                <span class="value">${criterion.rule_score}/100</span>
            </div>
            <div class="detail-row">
                <span class="label">Semantic Score:</span>
                <span class="value">${criterion.semantic_score}/100</span>
            </div>
            <div class="detail-row">
                <span class="label">Keywords Found:</span>
                <span class="value">${criterion.keywords_found.length > 0 ? criterion.keywords_found.join(', ') : 'None'}</span>
            </div>
            <div class="detail-row">
                <span class="label">Word Count:</span>
                <span class="value">${criterion.word_count}</span>
            </div>
        </div>

        <div class="criterion-feedback">
            <strong>💡 Feedback:</strong> ${criterion.feedback}
        </div>
    `;

    return card;
}

// Get score color
function getScoreColor(score) {
    if (score >= 80) return '#22c55e';
    if (score >= 60) return '#3b82f6';
    if (score >= 40) return '#f59e0b';
    return '#ef4444';
}

// Get score interpretation
function getScoreInterpretation(score) {
    if (score >= 90) return '🌟 Outstanding! Excellent communication skills.';
    if (score >= 80) return '✨ Very Good! Strong introduction with clear structure.';
    if (score >= 70) return '👍 Good! Solid introduction with room for minor improvements.';
    if (score >= 60) return '📝 Satisfactory. Consider adding more details in some areas.';
    if (score >= 50) return '⚠️ Needs Improvement. Try to cover more criteria.';
    return '❌ Poor. Significant improvements needed across multiple areas.';
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    document.getElementById('results').style.display = 'none';
}

// Export results as JSON
function exportResults() {
    if (!latestResults) {
        alert('No results to export');
        return;
    }

    const dataStr = JSON.stringify(latestResults, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = 'transcript-score-results.json';
    link.click();
    
    URL.revokeObjectURL(url);
}

// Allow Enter key to submit
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('transcript').addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            scoreTranscript();
        }
    });
});
