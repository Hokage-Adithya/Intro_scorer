"""
Flask REST API for transcript scoring
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scorer import get_scorer
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize scorer on startup (may take a moment to load the model)
scorer = None

@app.before_request
def initialize_scorer():
    """Initialize scorer before first request"""
    global scorer
    if scorer is None:
        scorer = get_scorer()

@app.route('/')
def index():
    """Serve the main UI"""
    return render_template('index.html')

@app.route('/api/score', methods=['POST'])
def score_transcript():
    """
    API endpoint to score a transcript
    
    Expected JSON input:
    {
        "transcript": "text of the student's introduction"
    }
    
    Returns JSON output with scores and feedback
    """
    try:
        # Get transcript from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No data provided. Please send JSON with a "transcript" field.'
            }), 400
        
        transcript = data.get('transcript', '').strip()
        
        if not transcript:
            return jsonify({
                'error': 'Transcript is empty. Please provide text to score.'
            }), 400
        
        # Score the transcript
        global scorer
        result = scorer.score_transcript(transcript)
        
        # Return the result
        return jsonify(result), 200
    
    except Exception as e:
        # Log error and return error response
        print(f"Error scoring transcript: {str(e)}")
        traceback.print_exc()
        return jsonify({
            'error': f'An error occurred while scoring: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'scorer_loaded': scorer is not None
    }), 200

if __name__ == '__main__':
    print("Starting Transcript Scorer API...")
    print("Loading AI models (this may take a moment)...")
    
    # Pre-initialize scorer
    scorer = get_scorer()
    
    print("\n" + "="*60)
    print("Server is ready!")
    print("Open your browser and go to: http://localhost:5000")
    print("="*60 + "\n")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
