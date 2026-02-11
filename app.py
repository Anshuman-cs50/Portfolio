from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Placeholder for ML model prediction
    return jsonify({'result': 'Prediction placeholder'})

if __name__ == '__main__':
    app.run(debug=True)
