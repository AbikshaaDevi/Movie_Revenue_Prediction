# Movie Revenue Prediction

This repository contains a **Movie Revenue Prediction** project that uses machine learning techniques to predict the revenue of movies based on various features such as budget, genre, cast, release date, and more.

## Features
- Data preprocessing and feature engineering for movie-related datasets
- Exploratory data analysis and visualization
- Model building using:
  - Linear Regression
  - Decision Trees and Random Forest
  - Gradient Boosting techniques (e.g., XGBoost, LightGBM)
- Model evaluation and tuning using cross-validation and error metrics

## Tech Stack
- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-learn, XGBoost, LightGBM**
- **Jupyter Notebook**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbikshaaDevi/Movie_Revenue_Prediction.git
   cd Movie_Revenue_Prediction
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the Jupyter notebooks for EDA and model training:
   ```bash
   jupyter notebook
   ```
2. Experiment with different models and hyperparameters to improve performance.

## Dataset
- The dataset typically includes information about movies such as budget, runtime, genre, production company, etc.
- Possible sources: [TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) or similar.

## Folder Structure
```
Movie_Revenue_Prediction/
│-- data/               # Raw and processed datasets
│-- notebooks/          # Jupyter notebooks for EDA and model building
│-- models/             # Trained models (if saved)
│-- requirements.txt    # Dependencies
│-- README.md           # Project documentation
```

## Future Improvements
- Deploy the model as a web app using Flask or Streamlit
- Use advanced feature engineering for better prediction accuracy
- Integrate external data (e.g., social media sentiment, box office trends)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
