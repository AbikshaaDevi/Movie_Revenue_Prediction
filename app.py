from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and features list
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('features.pkl', 'rb') as f:
    features = pickle.load(f)

# List of genres used in model (from features, skip numeric features)
genres = [feat for feat in features if feat not in ['budget', 'popularity', 'runtime']]

# Fixed exchange rate (1 USD ≈ 83 INR)
USD_TO_INR = 83

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', genres=genres, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read numeric inputs
        budget_inr = float(request.form['budget'])
        budget_usd = budget_inr / USD_TO_INR  # Convert to USD
        popularity = float(request.form['popularity'])
        runtime = float(request.form['runtime'])

        # Read genre selections as checkboxes
        selected_genres = request.form.getlist('genres')

        # Build input dictionary for model
        input_dict = {
            'budget': budget_usd,
            'popularity': popularity,
            'runtime': runtime
        }

        # For each genre, 1 if selected, else 0
        for genre in genres:
            input_dict[genre] = 1 if genre in selected_genres else 0

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict], columns=features)

        # Predict revenue in USD
        pred_revenue_usd = model.predict(input_df)[0]

        # Convert prediction to INR
        pred_revenue_inr = pred_revenue_usd * USD_TO_INR

        # Format prediction in crores for better readability
        pred_str = f"₹{pred_revenue_inr / 1e7:.2f} Crore"

        return render_template('index.html', genres=genres, prediction=pred_str)

    except Exception as e:
        return render_template('index.html', genres=genres, prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
