from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import uvicorn

# Load the saved model
pipeline = joblib.load('./model_pipeline.joblib')
print("Model loaded successfully:", type(pipeline))
# Create a FastAPI app
app = FastAPI(title="Fake News Detection API")
test_text = ["Breaking News: Scientists confirm the Earth is actually flat"]
test_prediction = pipeline.predict(test_text)[0]


# Define the input data model
class NewsItem(BaseModel):
    text: str

# Define function to convert numeric predictions to labels
def output_label(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

print(f"Test prediction: {test_prediction}, Label: {output_label(test_prediction)}")
# Create an endpoint for predictions
@app.post("/predict")
async def predict_news(news: NewsItem):
    # Make prediction
    prediction = pipeline.predict([news.text])[0]
    
    # Convert prediction to label
    result = output_label(prediction)
    
    # Return the prediction and confidence
    return {
        "text": news.text,
        "prediction": result,
        "prediction_code": int(prediction)
    }

# Optional: Add a simple health check endpoint
@app.get("/")
async def root():
    return {"status": "The Fake News Detection API is running!"}

# Run the API with uvicorn when the script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)