#/bin/bash
cd /Users/priyambodo/Desktop/Coding/00.github-priyambodo-at-google/public/priyambodo.com/priyambodo.com-iamgemini/v1.0

pip install --upgrade pip
python3 -m venv .virtualenv-priyambodo
source gemini-streamlit/bin/activate
pip install -r requirements.txt
pip install --upgrade google-cloud-aiplatform