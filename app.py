from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Form page for input
@app.route("/input")
def input_form():
    return render_template("input.html")

# Prediction result page
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Retrieve form data
        item_weight = float(request.form['item_weight'])
        item_fat_content = float(request.form['item_fat_content'])
        item_visibility = float(request.form['item_visibility'])
        item_type = float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year = float(request.form['outlet_establishment_year'])
        outlet_size = float(request.form['outlet_size'])
        outlet_location_type = float(request.form['outlet_location_type'])
        outlet_type = float(request.form['outlet_type'])

        # Example prediction logic (replace with your actual prediction code)
        prediction = 1234.56
        
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
