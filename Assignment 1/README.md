# SMS Spam Detection Project

This project implements a machine learning solution for detecting spam SMS messages. The system uses various text classification algorithms to identify whether a message is spam or legitimate (ham).

## Features

- Text preprocessing including:
  - Lowercase conversion
  - Stopword removal
  - Punctuation removal
  - Tokenization
- Exploratory data analysis with visualizations
- Implementation of multiple classifiers:
  - Decision Tree
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
- Hyperparameter tuning using GridSearchCV
- Model evaluation using precision, recall, and F1-score

## Dataset

The dataset contains SMS messages labeled as either spam or ham (non-spam). The data is split as follows:

- Training set: 70%
- Validation set: 10%
- Test set: 20%

## Notebooks

### [`prepare.ipynb`](./prepare.ipynb)

This notebook handles data preprocessing and exploratory analysis:

1. **Data Overview**:

   - The dataset contains SMS messages with two columns: category (spam/ham) and message text.
   - Messages are preprocessed by converting to lowercase, removing stopwords and punctuation, tokenizing the text, and retaining only alphanumeric words.

2. **Dataset Split**:

   - The data is split into training (70%), validation (10%), and test (20%) sets.

3. **Exploratory Analysis**:

   - Visualizes the distribution of spam vs ham messages using a pie chart.
   - Visualizes the most frequent words separately for spam and ham messages.

4. **Data Preprocessing**:
   - Defines a function to process text by converting to lowercase, removing stopwords and punctuation, and tokenizing.
   - Applies this function to the dataset and saves the processed data into CSV files for further use.

### [`train.ipynb`](./train.ipynb)

This notebook handles model training and evaluation:

1. **Data Loading and Preprocessing**:

   - Loads the preprocessed train, validation, and test datasets.
   - Removes any rows with missing values.
   - Merges the training and validation sets for better model performance.

2. **Feature Extraction**:

   - Converts text messages to TF-IDF vectors for machine learning input.
   - Displays the shape of the train and test data.

3. **Model Training and Hyperparameter Tuning**:

   - Implements and tunes four different classifiers: Decision Tree, Logistic Regression, Support Vector Machine (SVM), and Random Forest.
   - Uses GridSearchCV with 5-fold cross-validation to find optimal parameters for each model.

4. **Model Evaluation**:
   - Evaluates each classifier using classification reports (precision, recall, F1-score) and confusion matrices.
   - Provides sample predictions on test data.

## Usage

1. Create virtualenv:

   ```bash
   python -m virtualenv venv
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run `prepare.ipynb` and `train.ipynb` in order.

## Model Performance

The project evaluates multiple machine learning models using:

- Classification reports (precision, recall, F1-score)
- Confusion matrices
- Cross-validation scores

Each model is tuned using GridSearchCV with 5-fold cross-validation to find optimal parameters.

| Model               | Accuracy | Weighted F1-Score | Ham Precision | Ham Recall | Spam Precision | Spam Recall |
| ------------------- | -------- | ----------------- | ------------- | ---------- | -------------- | ----------- |
| Decision Tree       | 96%      | 0.965             | 0.98          | 0.98       | 0.89           | 0.85        |
| Logistic Regression | 98%      | 0.98              | 0.98          | 1          | 0.97           | 0.89        |
| SVM                 | 99%      | 0.99              | 0.99          | 1          | 0.99           | 0.91        |
| Random Forest       | 98%      | 0.98              | 0.98          | 1          | 0.99           | 0.88        |

- All models show strong performance with accuracy and F1-scores between 96-99%.
- The Logistic Regression, SVM and Random Forest models performed marginally better than the Decision Tree classifier.
- For spam detection specifically, the models show high precision (89-92%) and good recall (85-87%) on spam messages.
- They also maintained excellent performance on ham messages with both precision and recall around 98-99%.

> But, if I have to choose one, I think the `Support Vector Machine` will be the best choice as it outperforms others for all the metrics.
