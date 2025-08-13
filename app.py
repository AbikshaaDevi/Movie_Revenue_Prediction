from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model, scaler, and features
with open('ridge_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('features.pkl', 'rb') as f:
    features = pickle.load(f)

# Extract genre feature names (all except numeric ones)
numeric_features = ['budget', 'popularity', 'runtime']
genres = [feat for feat in features if feat not in numeric_features]

# Conversion rate USD <-> INR
USD_TO_INR = 83

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', genres=genres, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        budget_inr = float(request.form['budget'])
        popularity = float(request.form['popularity'])
        runtime = float(request.form['runtime'])
        selected_genres = request.form.getlist('genres')

        # Convert budget INR to USD (model trained on USD)
        budget_usd = budget_inr / USD_TO_INR

        # Build input dictionary for prediction
        input_dict = {
            'budget': budget_usd,
            'popularity': popularity,
            'runtime': runtime,
        }

        # Set genres 1 if selected else 0
        for genre in genres:
            input_dict[genre] = 1 if genre in selected_genres else 0

        # Convert to DataFrame with proper column order
        input_df = pd.DataFrame([input_dict], columns=features)

        # Scale numeric features using loaded scaler
        input_df[numeric_features] = scaler.transform(input_df[numeric_features])

        # Predict revenue in USD
        pred_revenue_usd = model.predict(input_df)[0]

        # Convert prediction back to INR
        pred_revenue_inr = pred_revenue_usd * USD_TO_INR

        # Format prediction in crores INR
        pred_str = f"₹{pred_revenue_inr / 1e7:.2f} Crore"

        return render_template('index.html', genres=genres, prediction=pred_str)

    except Exception as e:
        return render_template('index.html', genres=genres, prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
