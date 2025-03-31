# Climate Change Dashboard 🌎

Welcome to the Climate Change Dashboard! This interactive web application allows users to explore climate trends and make predictions about future climate conditions using machine learning models.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)


## Features

- Visualize historical climate data, including:
  - Arctic ice extent
  - Sea level rise
  - Temperature anomalies
- Filter data by year range using a sidebar slider.
- Predict future climate data from 2025 to 2050 using trained machine learning models.
- Download predictions as a CSV file.
- Interactive and user-friendly interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn (for model training and predictions)
- Joblib (for model serialization)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/chaviva16/climate_dashboard.git
   cd climate_dashboard
   
  2.Create a virtual environment (optional but recommended):
  python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install the required packages:
pip install -r requirements.txt

4.Ensure you have the necessary model files (arctic_model.pkl, sea_level_model.pkl, temperature_model.pkl) and the dataset (climate_data.csv) in the project directory.

## Usage
To run the Climate Change Dashboard, execute the following command:
streamlit run app.py
This will start a local server, and you can view the dashboard in your web browser at http://localhost:8501.

## Data
The dashboard uses a dataset containing historical climate data. The dataset should include the following columns:

Year: The year of the data point.
Arctic Ice (Million sq km): The extent of Arctic ice in million square kilometers.
Sea Level Rise (mm): The rise in sea level in millimeters.
Temperature Anomaly (°C): The temperature anomaly in degrees Celsius.

## Models
The dashboard utilizes pre-trained machine learning models to make predictions about future climate conditions. The models are saved in the following files:

arctic_model.pkl: Model for predicting Arctic ice extent.
sea_level_model.pkl: Model for predicting sea level rise.
temperature_model.pkl: Model for predicting temperature anomalies.
