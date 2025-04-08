# veritas-backend

A simple  Fake News Detection system built using Python, scikit-learn, and FastAPI. This project classifies news articles as Fake or Not Fake using natural language processing (NLP) and machine learning techniques.

🚀 Features
Training a Decision Tree Classifier using TF-IDF vectorization

Evaluation using classification metrics (accuracy, precision, recall, F1-score)

Easy-to-use REST API built with FastAPI

Ready-to-use model pipeline for inference and deployment

🧠 Model Training
The model is trained on two datasets:

Fake.csv (Fake news articles)

True.csv (Genuine news articles)

Steps:
Data cleaning and preprocessing (removing noise, punctuation, etc.)

Label encoding (0 for Fake, 1 for Real)

TF-IDF vectorization to convert text to numeric format

Splitting the data into training and testing sets

Training a Decision Tree Classifier

Saving the trained pipeline using joblib

🔍 Sample Prediction
manual_testing("Breaking News: Scientists confirm the Earth is actually flat and NASA has been hiding the truth for decades", model)
Output: Fake News
🌐 API (FastAPI)
You can serve predictions via a RESTful API:

Endpoints
GET / — Health check

POST /predict — Submit news content and get a prediction

Sample request:
json
Copy
Edit
POST /predict
{
  "text": "Breaking: The Moon landing was staged!"
}
Sample response:
json
Copy
Edit
{
  "text": "Breaking: The Moon landing was staged!",
  "prediction": "Fake News",
  "prediction_code": 0
}
🛠 Tech Stack
Python

scikit-learn

FastAPI

Pandas, NumPy

Joblib

Uvicorn (for running the API)

⚙️ Run the Project
1. Install dependencies:
   pip install -r requirements.txt

3. Run the API:
   uvicorn main:app --reload

