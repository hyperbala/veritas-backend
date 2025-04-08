import joblib

# Load the model
MODEL_PATH = "model.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()
