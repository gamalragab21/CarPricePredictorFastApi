
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
# Define the input data model using BaseModel
from pydantic import BaseModel

class Car(BaseModel):
    doors: str
    wheel: str
    levy: float
    engine_volume: float
    mileage: int
    cylinders: int
    airbags: int
    model: str
    category: str
    leather_interior: str
    fuel_type: str
    gear_box_type: str
    drive_wheels: str
    engine_turbo: int
    age: int
    manufacturer: str

# Define a class for the singleton model loader
class ModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def get_model(self):
        if self.model is None:
            self.model = joblib.load(self.model_path)
        return self.model

# Create an instance of the model loader
car_model_loader = ModelLoader('carPricePredictorModel.pkl')

origins = [
    "https://localhost:7192",
    # Add any other allowed origins here
]

# Create a FastAPI application instance
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to predict car price
@app.post("/predict")
async def predict_car_price(car: Car):
    try:
        # Convert input data to DataFrame
        df_request = pd.DataFrame([car.dict()])

        # Load the pre-trained model and make a prediction
        model = car_model_loader.get_model()
        prediction = model.predict(df_request)

        # Round the predicted car price to two decimal places
        rounded_price = round(float(prediction[0]), 2)

        return {'message': 'Prediction successful', 'status': 200, "prediction": rounded_price}

    except Exception as e:
        print(e.with_traceback)
        return {"message": f'Please review your request body, maybe it contains invalid data: {str(e)}'}

# Root endpoint
@app.get('/')
async def root():
    return {"message": "Welcome to the Car Price Predictor API"}
