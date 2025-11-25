# BAIB Assignment 2: Hotel Reservation Fulfillment Prediction

## Project Overview

This project implements a machine learning model to predict whether a hotel reservation will be fulfilled or not at the time a customer makes a reservation. The model is designed to be deployed in an online booking system to provide real-time predictions and help the travel operator improve fulfillment rates.

## Problem Statement

As a team of data analysts working for a travel operator, we are tasked with:
- Creating a model that predicts if a reservation will be eventually fulfilled or not (or the probability of fulfilling)
- Deploying the model to perform predictions directly in the online system after each user makes a booking
- Extracting insights to investigate which actions could improve the fulfillment rate

## Dataset

The training dataset is provided in `data/reservations.csv`. The dataset contains information about hotel visits with the following key columns:

- **Target variable**: `status` - the status of the stay after check-out (cancelled, no-show, checked out correctly)
- **Temporal features**: `year`, `month`, `day_of_month`, `reservation_days_advance`, `status_date`
- **Reservation details**: `number`, `room_type`, `weekend_nights`, `week_nights`, `meal`, `deposit`
- **Guest information**: `num_adults`, `num_children`, `num_babies`, `returning`, `CRM`, `segment`
- **Hotel information**: `name_hotel`, `room_assigned`, `operator`, `entreprise`
- **Behavioral features**: `reservation_changes`, `waiting_list`, `num_cancellations`, `num_bookings_not_canceled`, `special_requests`
- **Financial features**: `average_rate`, `total_spending`, `num_vehicles`
- **Derived features**: `total_length_of_stay`

See `data/README.md` for detailed dataset schema and description.

## Project Structure

```
IAI_Assignment2/
│
├── data/
│   ├── reservations.csv                 # provided training dataset
│   └── README.md                        # describe dataset and schema
│
├── src/
│   ├── data_prep.py                     # all preprocessing functions
│   ├── features.py                      # feature engineering functions
│   ├── model.py                         # training pipeline (required deliverable)
│   ├── evaluate.py                      # cv metrics / test evaluation
│   └── utils.py                         # helpers (logging, timing)
│
├── models/
│   └── best_model.pkl                   # trained model saved via joblib
│
├── notebooks/
│   ├── 01_initial_eda.ipynb             # exploratory analysis
│   ├── 02_feature_engineering.ipynb     # experiments
│   └── 03_model_selection.ipynb         # cross-validation and hyperparams
│
├── reports/
│   └── assignment_report.pdf            # final 5-page report
│
├── requirements.txt                     # dependencies (sklearn, pandas, numpy)
├── .gitignore                           # ignore data artifacts
├── pyproject.toml                       # project configuration
└── README.md                            # this file
```

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- scikit-learn
- pandas
- numpy
- joblib

## How to Run

### Training the Model

To train the model, run the main training script:

```bash
python src/model.py
```

This script will:
1. Load and preprocess the data from `data/reservations.csv`
2. Construct features and prepare the dataset
3. Train the model using cross-validation
4. Evaluate the model performance
5. Save the trained model to `models/best_model.pkl`

### Model Output

The trained model will be saved as `models/best_model.pkl` using joblib. The script will also output:
- Cross-validation metrics
- Test set evaluation metrics
- Performance reports

## Deliverables

### Part I: Create the Model (7 points)

The `model.py` script includes:
- Label vector construction based on the `status` column
- Feature engineering and data preparation
- Model training with cross-validation
- Appropriate performance metrics

### Part II: Model Evaluation (3 points)

The model will be evaluated on an unseen test set with the same distribution to simulate deployment on new data.

### Report

A 5-page report (`reports/assignment_report.pdf`) includes:
- **Max 2 pages**: Data preparation and modeling steps
- **Max 2 pages**: Metrics and interpretation
- **Max 1 page**: Recommendations for strategies to augment the fulfillment rate

## Methodology

The model construction process involves:
1. **Data Exploration**: Initial EDA to understand the dataset (see `notebooks/01_initial_eda.ipynb`)
2. **Feature Engineering**: Creating informative features and selecting relevant ones (see `notebooks/02_feature_engineering.ipynb`)
3. **Model Selection**: Cross-validation and hyperparameter tuning (see `notebooks/03_model_selection.ipynb`)
4. **Training**: Final model training on the complete dataset
5. **Evaluation**: Performance assessment using appropriate metrics

## Notes

- The model should be trained on all available data in `reservations.csv`
- The model will be evaluated on an unseen test set that follows the same distribution
- Feature selection should consider which features are informative and appropriate for prediction
- All features should be tried initially to understand their impact

## Assessment

The exercise evaluates:
- Correctness in implementation (adequate and complete steps, correct use of Python functions)
- Correct application of methodology
- Correctness and adequateness of the report's content
- Compliance with class learnings
- Final metric performance on the test dataset

