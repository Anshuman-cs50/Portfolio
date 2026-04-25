import json
import os
from flask import Flask, render_template, jsonify
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    data_file = Path("data/achievements.json")
    achievements = {"hackathons": [], "certifications": []}
    
    if data_file.exists():
        with open(data_file, "r") as f:
            achievements = json.load(f)
            
    return render_template('index.html', achievements=achievements)

@app.route('/predict', methods=['POST'])
def predict():
    # Placeholder for ML model prediction
    return jsonify({'result': 'Prediction placeholder'})

if __name__ == '__main__':
    app.run(debug=True)
