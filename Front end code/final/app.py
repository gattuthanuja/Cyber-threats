from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load your model
model = load_model("my_UNSW_model/my_final_model.h5")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        try:
            # Get input values
            inputs = [float(request.form[f"feature{i}"]) for i in range(1, 9)]
            inputs = np.array([inputs])
            
            # Predict
            prediction = model.predict(inputs)
            result = "Threat Detected" if prediction[0][0] == 1 else "No Threat"
            return render_template("prediction.html", prediction=result)
        except Exception as e:
            return render_template("prediction.html", prediction=f"Error: {str(e)}")
    return render_template("prediction.html")

@app.route("/metrics")
def metrics():
    return render_template("metrics.html")

@app.route("/flowchart")
def flowchart():
    return render_template("flowchart.html")

if __name__== "__main__":
    app.run(debug=True)