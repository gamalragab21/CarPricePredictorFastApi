# Car Price Prediction with EDA

This repository contains a Jupyter Notebook for car price prediction, along with exploratory data analysis (EDA) of the dataset. The notebook explores a dataset of car features and uses machine learning algorithms to predict the price of a car based on its characteristics.

![Car Image](https://cdn.dribbble.com/users/8156988/screenshots/16260376/media/d72c6c8fe5a5cded14961afbe4590e2d.gif)

## Kaggle Notebook

You can find the notebook used for car price prediction and EDA on Kaggle by following this link: [Car Price Prediction Notebook on Kaggle](https://www.kaggle.com/code/gamalragab/eda-car-price-prediction-with-97-accuracy)

## Dataset

The dataset used in this notebook contains various attributes of cars, such as make, model, year, mileage, engine size, etc. It is used to train and evaluate machine learning models to predict the price of a car. The dataset is included in the repository as 'car_data.csv'.

## Notebook Contents

The notebook includes the following sections:

1. **Data Exploration and Analysis (EDA)**: In this section, we analyze and visualize the dataset to gain insights into the car features, their distributions, correlations, and relationships with the price. The EDA provides a comprehensive understanding of the dataset, identifies any outliers or missing values, and helps in feature selection for the prediction model.

2. **Data Preprocessing**: This section handles missing values, encodes categorical variables, and scales numerical features to prepare the data for model training.

3. **Feature Selection**: Here, we select the most relevant features that have the most impact on predicting car prices. This helps in improving model performance and reducing complexity.

4. **Model Building**: In this step, we train and evaluate various machine learning models, such as linear regression, random forest, and gradient boosting, for car price prediction. We compare their performance and choose the best model based on evaluation metrics.

5. **Model Evaluation**: This section assesses the performance of the trained models using appropriate evaluation metrics, such as mean squared error (MSE) or mean absolute error (MAE). It helps us understand how well our models are performing in predicting car prices.

6. **Conclusion**: Finally, we summarize the findings, discuss the accuracy achieved in predicting car prices, and provide insights gained from the EDA analysis. We also discuss potential areas for improvement or further experimentation.

## Usage

To run the notebook locally, you can follow these steps:

1. **Clone the Repository**: Clone this repository by running the following command in your terminal or command prompt:
   `git clone https://github.com/gamalragab21/car-price-eda-prediction.git`

2. **Install Dependencies**: Install the required dependencies by running the following command:
   `pip install -r requirements.txt`


3. **Open the Notebook**: Open the notebook file, `car_price_prediction.ipynb`, using Jupyter Notebook or JupyterLab.

4. **Execute the Notebook**: Execute the cells in sequential order to reproduce the exploratory data analysis and predictions.

5. **Interact with the Web Service**: Start the FastAPI application by running the following command:

### python CarPredictorApp.py

Once the application is running, you can send a POST request to `https://car-price-prediction-e99b.onrender.com/predict` with a JSON payload containing a car object. Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
   {
    "doors": "4",
    "wheel": "Left",
    "levy": 100,
    "engine_volume": 2.0,
    "mileage": 5000,
    "cylinders": 4,
    "airbags": 6,
    "model": "Camry",
    "category": "Sedan",
    "leather_interior": "Yes",
    "fuel_type": "Petrol",
    "gear_box_type": "Automatic",
    "drive_wheels": "Front",
    "engine_turbo": 1,
    "age": 5,
    "manufacturer": "Toyota"
}
}' https://car-price-prediction-e99b.onrender.com/predict
```


The response will include the predicted price of the car.

Feel free to explore the notebook, delve into the EDA section, and experiment with different models or techniques to further improve the accuracy of car price prediction.

## Contributing
If you have any suggestions, improvements, or would like to contribute to this project, please feel free to open an issue or submit a pull request.

# Additional Information
## Dependencies
Make sure you have the following dependencies installed:

Python 3.x
Jupyter Notebook
FastAPI
You can install the required Python packages by running the following command:
```bash pip install -r requirements.txt ```

## Deployment
The trained model is deployed as a web service using FastAPI and hosted on the Render platform. To access the car price prediction API, follow these steps:

1. Start the FastAPI application by running the following command: `python CarPredictorApp.py`
2. Once the application is running, you can send a POST request to https://car-price-prediction-e99b.onrender.com/predict with a JSON payload containing a car object to get the predicted price.

## Contact
For any inquiries or questions, feel free to reach out to  **Gamal Ragab**.







