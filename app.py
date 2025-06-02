from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('heart_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        input_values = [float(request.form.get(feat)) for feat in [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]]
        # Convert to numpy array
        final_input = np.array([input_values])

        # Predict
        prediction = model.predict(final_input)[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return render_template('index.html', prediction=result)
    
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
