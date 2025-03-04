# SMS Spam Detection Project

This assignment adds `dvc` and `mlflow` to better track the data and models.

## Project Overview

- Text preprocessing with lowercase conversion, stopword removal, and tokenization
- Feature extraction using TF-IDF vectorization
- Multiple classifiers: Decision Tree, Logistic Regression, SVM, Random Forest
- Hyperparameter optimization and model evaluation
- DVC for data versioning
- MLflow for experiment tracking

## Dataset Structure

- Training set: 70% of data
- Validation set: 10% of data
- Test set: 20% of data

## Project Files

### [`prepare.ipynb`](./prepare.ipynb)

- DVC setup with Google Drive remote storage
- Data preprocessing and train/validation/test splits
- Dataset version control and tracking

### [`train.ipynb`](./train.ipynb)

- Text preprocessing and vectorization
- Model training with MLflow tracking
- Hyperparameter tuning and evaluation

## Model Results

AUCPR Scores:
- SVM: 0.9419
- Random Forest: 0.9419
- Logistic Regression: 0.9329 
- Decision Tree: 0.8143

SVM selected as final model based on performance and simplicity.
