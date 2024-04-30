from flask import Flask, render_template, request, redirect
import numpy as np
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('index.html', prediction_text = "You have no heart disease" if prediction == 0  else "You have heart disease")

if __name__ == "__main__":
    app.run(debug=True)