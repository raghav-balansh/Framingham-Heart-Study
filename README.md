# Framingham-Heart-Study

<h3>This is the Heart Decease Classifier</h3>


This project provides a user-friendly web interface for assessing an individual's risk of developing heart disease based on the Framingham Heart Study data. It leverages a machine learning model trained on historical data to generate risk predictions.

**Features:**

- health information.
- Clear and concise instructions for each input field.
- Informative descriptions of health parameters, including reference ranges where applicable.

**Getting Started:**

1. **Prerequisites:**
    - Python (version 3.12 recommended)
    - Additional dependencies (Flask, scikit-learn, pickle, numpy, pandas)
    - A trained machine learning model(model.pickle)

2. **Installation:**
    b. Install dependencies: `pip install -r requirements.txt` 

3. **Running the Application:**
    b. Start the development server: `python app.py` 
    c. Access the application in your web browser, typically at `http://127.0.0.1:5000/` 

**Usage:**

1. Enter your health information accurately in the designated fields.
2. Click the "Predict Risk" button.
3. The application will display your predicted risk of developing heart disease.

**Disclaimer:**

- This tool is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare provider for diagnosis and treatment planning.
