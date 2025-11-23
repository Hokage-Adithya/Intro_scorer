# 🎬 SCREEN RECORDING GUIDE

## Video Recording Checklist for Nirmaan AI Case Study Submission

Record your screen while demonstrating the following steps. Aim for a 3-5 minute video that clearly shows your application working.

---

## 🔴 Recording Steps

### Part 1: Project Overview (30 seconds)
1. **Show the project folder structure**
   - Open File Explorer to `d:\nirmaan\transcript-scorer`
   - Show all files: app.py, scorer.py, rubric.py, templates/, static/, etc.
   - Briefly explain: "This is the complete project structure"

### Part 2: Installation & Setup (1 minute)
2. **Open PowerShell/Terminal**
   - Navigate to project directory: `cd d:\nirmaan\transcript-scorer`
   - Show: `Get-ChildItem` to list files
   
3. **Show requirements**
   - Open `requirements.txt` in notepad or VS Code
   - Explain: "These are the dependencies: Flask, sentence-transformers, etc."

4. **Install dependencies (optional - can skip if already done)**
   - `pip install -r requirements.txt`
   - Or just show it's already installed

### Part 3: Running the Application (30 seconds)
5. **Start the server**
   - Run: `python app.py`
   - Show the console output:
     - "Loading sentence transformer model..."
     - "Scorer initialized successfully!"
     - "Server is ready! Open your browser and go to: http://localhost:5000"

### Part 4: Demonstrate the Web Interface (2-3 minutes)
6. **Open the browser**
   - Navigate to: `http://localhost:5000`
   - Show the beautiful UI with the title "Student Introduction Scorer"

7. **Load the sample transcript**
   - Click the **"Load Sample"** button
   - Show that Muskan's introduction appears in the text area
   - Read a line or two: "Hello everyone, myself Muskan..."

8. **Score the transcript**
   - Click **"Score Transcript"** button
   - Show the loading animation
   - Wait for results (2-3 seconds)

9. **Explain the results**
   - **Overall Score**: Point to the large score circle (should be 70-85)
   - **Total Words**: Show the word count
   - **Score Interpretation**: Read the interpretation message

10. **Show detailed breakdown**
    - Scroll down to the criteria cards
    - Explain each criterion:
      - **Personal Introduction**: Score, keywords found, feedback
      - **Family Description**: Show the score bar and details
      - **Academic Interests**: Point out the semantic score
    - Show at least 3-4 different criteria cards

11. **Demonstrate the feedback**
    - Read aloud one or two feedback messages
    - Example: "Excellent coverage of personal introduction! Found keywords: myself, age, class, school..."

### Part 5: Test with Custom Input (Optional - 1 minute)
12. **Clear and test with new text**
    - Click **"Clear"** button
    - Type a short introduction manually:
      ```
      Hi, I am John, 14 years old from St. Mary's School. 
      I live with my parents and one sister.
      ```
    - Click **"Score Transcript"**
    - Show that it gives a lower score (since it's incomplete)
    - Point out which criteria scored low and why

### Part 6: Export Results (30 seconds)
13. **Export functionality**
    - Click **"Export as JSON"** button
    - Show the downloaded JSON file
    - Open it in notepad to show the structured data:
      ```json
      {
        "overall_score": 78.5,
        "total_words": 92,
        "criteria_scores": [...]
      }
      ```

### Part 7: Explain the Scoring Logic (1 minute)
14. **Show the code briefly**
    - Open `scorer.py` in VS Code
    - Scroll to show:
      - `rule_based_score` function (keyword matching)
      - `semantic_score` function (NLP similarity)
      - `compute_criterion_score` (combining both)
    - Explain: "This combines rule-based keywords and AI semantic analysis"

15. **Show the rubric**
    - Open `rubric.py`
    - Show the criteria with weights:
      - Personal Introduction: 20%
      - Family Description: 15%
      - Academic Interests: 15%
      - etc.

### Part 8: Closing (30 seconds)
16. **Stop the server**
    - Go back to terminal
    - Press `Ctrl+C` to stop
    - Show: "Server stopped successfully"

17. **Final words**
    - "This is my complete submission for the Nirmaan AI Case Study"
    - "The application analyzes student introductions using AI and provides detailed feedback"
    - "Thank you!"

---

## 📋 Recording Tools & Tips

### Recommended Screen Recording Software
- **Windows**: 
  - Xbox Game Bar (Win+G) - Built-in, free
  - OBS Studio - Professional, free
  - Loom - Easy to use, free tier available
  - ShareX - Free and powerful

### Recording Tips
1. **Clear your desktop** - Close unnecessary windows
2. **Set resolution** - 1920x1080 recommended
3. **Use a good microphone** - Built-in or headset
4. **Speak clearly** - Explain what you're doing
5. **Go slow** - Don't rush through steps
6. **Show, don't tell** - Demonstrate actual functionality
7. **Zoom in** if needed - Make text readable
8. **Edit if needed** - Remove mistakes or dead time

### What to Say During Recording

**Introduction:**
> "Hello! This is my submission for the Nirmaan AI internship case study. I've built a Student Introduction Scorer that uses AI to analyze and score self-introductions. Let me walk you through the project."

**During Demo:**
> "As you can see, the application is running on localhost:5000. I'll now load the sample transcript provided - Muskan's introduction. When I click Score Transcript, the AI analyzes the text using both keyword matching and semantic similarity. The overall score is [X], which is [interpretation]. Each criterion is scored separately, as you can see here..."

**Closing:**
> "The complete code is available in my GitHub repository with detailed README and deployment instructions. Thank you for watching!"

---

## 📤 Submission Format

After recording:

1. **Save the video** as: `[YourName]_Nirmaan_AI_CaseStudy_Demo.mp4`
2. **Upload to**:
   - YouTube (Unlisted)
   - Google Drive
   - Loom
   - Or any video hosting service

3. **Include the video link** in your submission form along with:
   - GitHub repository URL
   - Deployed app URL (if applicable)
   - This README

---

## ⏱️ Timing Breakdown
- Part 1: 30s
- Part 2: 1min
- Part 3: 30s
- Part 4: 2-3min
- Part 5: 1min (optional)
- Part 6: 30s
- Part 7: 1min
- Part 8: 30s

**Total: 5-7 minutes**

---

## ✅ Final Checklist Before Recording

- [ ] Application runs without errors
- [ ] All dependencies are installed
- [ ] Sample transcript loads correctly
- [ ] Scoring works and returns results
- [ ] Export JSON function works
- [ ] Desktop is clean and professional
- [ ] Microphone is working
- [ ] Recording software is set up
- [ ] You're ready to explain the project clearly

---

**Good luck with your recording! 🎥**
