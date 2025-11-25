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

**Python Version**: Python 3.11 or higher is required.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- scikit-learn
- pandas
- numpy
- joblib

### Development Dependencies

For code quality checks (linting, formatting), install:

```bash
pip install ruff black
```

These are used by the CI/CD pipeline and can be run locally for code quality checks.

## Development

### Code Quality

Before committing, you can run local validation:

```bash
# Run project structure and syntax validation
python scripts/validate.py

# Format code with Black
black src/

# Lint code with Ruff
ruff check src/
```

### CI/CD

This project uses GitHub Actions for continuous integration. The CI pipeline runs automatically on every push and pull request.

#### How It Works

**Automatic Triggers:**
- Runs on every push to `main` or `develop` branches
- Runs on every pull request targeting `main` or `develop`
- All checks must pass for the workflow to succeed

**What Gets Checked:**

The CI pipeline runs 4 parallel jobs:

1. **Code Quality Checks** (`lint-and-format`)
   - ✅ Code formatting with Black (ensures consistent style)
   - ✅ Code linting with Ruff (catches errors and style issues)
   - ✅ Python syntax validation (catches syntax errors)

2. **Project Structure Validation** (`validate-structure`)
   - ✅ Verifies all required files exist:
     - `src/model.py`, `src/data_prep.py`, `src/features.py`, `src/evaluate.py`, `src/utils.py`
     - `requirements.txt`, `README.md`, `pyproject.toml`

3. **Import Validation** (`import-validation`)
   - ✅ Tests that all Python modules can be imported
   - ✅ Validates Python syntax in all source files
   - Gracefully handles empty files (won't fail if files are still being developed)

4. **Dependency Validation** (`dependency-check`)
   - ✅ Validates `requirements.txt` format
   - ✅ Checks for common formatting issues (e.g., quoted packages)

#### Workflow: Before Pushing

**1. Run Local Validation (Recommended)**
```bash
# Run all validation checks locally
python scripts/validate.py
```

This runs the same checks locally so you can fix issues before pushing.

**2. Format Your Code**
```bash
# Auto-format code with Black
black src/

# Check what would be formatted (without changing files)
black --check src/
```

**3. Lint Your Code**
```bash
# Run linter to catch issues
ruff check src/

# Auto-fix issues where possible
ruff check src/ --fix
```

**4. Commit and Push**
```bash
git add .
git commit -m "Your commit message"
git push
```

The CI will automatically run when you push.

#### Viewing CI Results

**On GitHub:**
1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. You'll see a list of workflow runs
4. Click on a run to see detailed results
5. Green checkmark ✅ = all checks passed
6. Red X ❌ = some checks failed (click to see details)

**Understanding Failures:**

- **Formatting Error**: Run `black src/` locally and commit the changes
- **Linting Error**: Fix the issues shown by Ruff, or run `ruff check src/ --fix`
- **Syntax Error**: Fix the Python syntax error in the file mentioned
- **Missing File**: Ensure all required files exist in the project
- **Import Error**: Check that your imports are correct and dependencies are installed
- **Dependency Format Error**: Fix the format in `requirements.txt` (no quotes, proper version specifiers)

#### Best Practices

1. **Run validation locally first**: Catch issues before pushing
2. **Fix formatting automatically**: Use `black src/` to auto-format
3. **Check CI before merging PRs**: Ensure all checks pass
4. **Read error messages**: CI provides specific feedback on what failed

#### Example Workflow

```bash
# 1. Make your changes
# ... edit files ...

# 2. Validate locally
python scripts/validate.py

# 3. Format code
black src/

# 4. Check linting
ruff check src/

# 5. If all good, commit and push
git add .
git commit -m "Add feature X"
git push

# 6. Check GitHub Actions tab for CI results
```

#### Troubleshooting

**CI fails but works locally:**
- Ensure you're using Python 3.9+
- Check that all dependencies are in `requirements.txt`
- Verify file paths are correct (CI uses Linux paths)

**Formatting keeps failing:**
- Run `black src/` and commit the formatted code
- Consider adding a pre-commit hook (see below)

**Import errors in CI:**
- Make sure all imports are at the top of files
- Check that you're not using relative imports incorrectly
- Verify all dependencies are listed in `requirements.txt`

See `.github/workflows/ci.yml` for the complete CI configuration.

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

