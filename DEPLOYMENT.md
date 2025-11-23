# 📖 DEPLOYMENT GUIDE - Student Introduction Scorer

## Complete Step-by-Step Deployment Instructions

---

## 🖥️ LOCAL SERVER DEPLOYMENT (Windows)

### Prerequisites Check
Before starting, ensure you have:
- [ ] Python 3.8 or higher installed
- [ ] pip (comes with Python)
- [ ] Internet connection (for downloading AI models)
- [ ] At least 500MB free disk space

### Step-by-Step Installation

#### Step 1: Verify Python Installation
Open PowerShell and run:
```powershell
python --version
```
Expected output: `Python 3.8.x` or higher

If not installed, download from: https://www.python.org/downloads/

#### Step 2: Navigate to Project Directory
```powershell
cd d:\nirmaan\transcript-scorer
```

#### Step 3: Create Virtual Environment (RECOMMENDED)
This keeps dependencies isolated from your system Python.

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

**Note:** If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Your prompt should now show `(venv)` at the beginning.

#### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

**Installation time:** 2-5 minutes (downloads ~200MB of packages)

**What gets installed:**
- Flask (web framework)
- sentence-transformers (AI model)
- numpy, scikit-learn (supporting libraries)
- flask-cors (for API access)

#### Step 5: First-Time Model Download
The AI model will be downloaded automatically on first run (~80MB).

```powershell
python app.py
```

**Expected output:**
```
Loading sentence transformer model...
Downloading model files... (first time only)
Scorer initialized successfully!

============================================================
Server is ready!
Open your browser and go to: http://localhost:5000
============================================================

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

#### Step 6: Access the Application
1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. You should see the Student Introduction Scorer interface

#### Step 7: Test the Application
1. Click **"Load Sample"** button to load Muskan's introduction
2. Click **"Score Transcript"** button
3. Wait 2-3 seconds for AI analysis
4. View the results with overall score and detailed breakdown

### Stopping the Server
Press `Ctrl+C` in the PowerShell window running the server.

### Restarting the Server
```powershell
# If virtual environment is not active
.\venv\Scripts\Activate.ps1

# Run the app
python app.py
```

---

## 🌐 CLOUD DEPLOYMENT OPTIONS

### Option A: AWS EC2 Free Tier

#### Prerequisites
- AWS account with free tier access
- Basic knowledge of SSH/PuTTY

#### Steps

**1. Launch EC2 Instance**
```
- Go to AWS Console → EC2
- Click "Launch Instance"
- Choose: Ubuntu Server 22.04 LTS
- Instance type: t2.micro (free tier)
- Create/select key pair
- Security group: Allow HTTP (port 80) and SSH (port 22)
- Launch instance
```

**2. Connect to Instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

**3. Install Dependencies**
```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Clone or upload your project
cd ~
mkdir transcript-scorer
cd transcript-scorer
# Upload files via SCP or git clone
```

**4. Setup Application**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 app.py
```

**5. Access Application**
```
http://your-ec2-public-ip:5000
```

**6. Run in Background (Optional)**
```bash
# Install screen
sudo apt install screen -y

# Start screen session
screen -S scorer

# Run app
python3 app.py

# Detach: Ctrl+A then D
# Reattach: screen -r scorer
```

---

### Option B: Heroku Deployment

#### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

#### Steps

**1. Install Heroku CLI**
Download from: https://devcenter.heroku.com/articles/heroku-cli

**2. Prepare Project**
Create `Procfile` in project root:
```
web: python app.py
```

Modify `app.py` to use PORT environment variable:
```python
# At the end of app.py, change:
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```

**3. Deploy**
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Push code
git init
git add .
git commit -m "Initial commit"
git push heroku main

# Open app
heroku open
```

---

### Option C: PythonAnywhere (Easiest)

#### Steps

**1. Create Account**
- Go to: https://www.pythonanywhere.com
- Sign up for free account

**2. Upload Files**
- Go to "Files" tab
- Create folder: `/home/yourusername/transcript-scorer`
- Upload all project files

**3. Create Virtual Environment**
Open Bash console:
```bash
mkvirtualenv --python=/usr/bin/python3.8 scorer-env
pip install -r transcript-scorer/requirements.txt
```

**4. Configure Web App**
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration"
- Python version: 3.8
- Configure WSGI file to point to your app.py

**5. Access App**
```
http://yourusername.pythonanywhere.com
```

---

## 🔧 TROUBLESHOOTING

### Common Issues

**Issue 1: "Python not recognized"**
Solution: Add Python to PATH during installation

**Issue 2: "Permission denied" on virtual environment**
Solution: Run PowerShell as Administrator or change execution policy

**Issue 3: "Module not found" errors**
Solution: Ensure virtual environment is activated, reinstall requirements

**Issue 4: Port 5000 already in use**
Solution: Change port in app.py or kill process using port 5000:
```powershell
# Find process
netstat -ano | findstr :5000

# Kill process (replace PID)
taskkill /PID <PID> /F
```

**Issue 5: Slow first request**
Solution: Normal! AI model loads on first request. Subsequent requests are fast.

**Issue 6: Model download fails**
Solution: Check internet connection. Manual download from:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

---

## 📊 PERFORMANCE NOTES

- **First startup:** 30-60 seconds (model loading)
- **First request:** 3-5 seconds (model initialization)
- **Subsequent requests:** < 1 second
- **Memory usage:** ~500MB (for AI model)
- **Concurrent users:** Up to 10 on free tier

---

## 🎥 VIDEO RECORDING CHECKLIST

When recording your demo video, show:

1. [ ] Opening PowerShell/Terminal
2. [ ] Navigating to project directory
3. [ ] Activating virtual environment
4. [ ] Running `python app.py`
5. [ ] Server startup messages
6. [ ] Opening browser to localhost:5000
7. [ ] Loading sample transcript
8. [ ] Clicking "Score Transcript"
9. [ ] Showing results with scores and feedback
10. [ ] Testing with custom text
11. [ ] Exporting JSON results
12. [ ] Showing the JSON file content

---

## 📞 SUPPORT

If you encounter issues:

1. Check this guide first
2. Review error messages carefully
3. Search error on Google/StackOverflow
4. Contact: jassmesh@nirmaan.education

---

## ✅ DEPLOYMENT VERIFICATION

After deployment, verify:

- [ ] Homepage loads correctly
- [ ] Sample button loads Muskan's transcript
- [ ] Score button analyzes and returns results
- [ ] Overall score displays (70-85 range expected)
- [ ] All 7 criteria show individual scores
- [ ] Feedback messages are meaningful
- [ ] Export JSON button works
- [ ] API endpoint `/api/score` responds to POST requests

---

**Last Updated:** November 23, 2025  
**Version:** 1.0  
**Author:** Nirmaan AI Intern Candidate
