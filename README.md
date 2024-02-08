# House Prediction Model Deployment

## Project Overview

This project is a machine learning model that predicts house prices based on various features such as the number of bedrooms, location, size, and more. The model is trained using the California Housing dataset and deployed using Flask.
## Getting Started

### Prerequisites

The following software and libraries need to be installed:
- Python 3.7+
- Scikit-learn
- Flask
- Install the necessary packages:
- pip install -r requirements.txt
Usage
To use the project, run the Flask application:
python app.py
Model
The model used in this project is a Random Forest Regressor, chosen for its ability to handle non-linear data and its robustness to outliers. The model was trained on 80% of the data, with the remaining 20% used for validation.

Deployment
The model is deployed as a Flask web app. Users can input the features of a house, and the model will return a predicted price. 
