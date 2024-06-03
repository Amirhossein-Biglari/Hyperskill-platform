import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set the random seed for reproducibility
np.random.seed(52)

# Function to convert 'Embarked' column values to numerical values
def convert_embarked(x):
    if x == 'S':
        return 0
    elif x == 'C':
        return 1
    else:
        return 2

if __name__ == '__main__':
    # Read the Titanic dataset from CSV file
    data = pd.read_csv('Stage 1/titanic.csv')

    # Drop unnecessary columns
    data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    # Drop rows with missing values
    data.dropna(inplace=True)

    # Separate the target variable 'Survived' and convert it to integer
    y = data['Survived'].astype(int)
    # Separate the features from the target variable
    X = data.drop('Survived', axis=1)

    # Convert 'Sex' column to numerical values: 0 for male, 1 for female
    X['Sex'] = X['Sex'].apply(lambda x: 0 if x == 'male' else 1)
    # Convert 'Embarked' column to numerical values using the convert_embarked function
    X['Embarked'] = X['Embarked'].apply(lambda x: convert_embarked(x))

    # Split the data into training and validation sets, maintaining the distribution of target variable
    X_train, X_val, y_train, y_val = train_test_split(X.values, y.values, stratify=y, train_size=0.8)

    # Initialize the DecisionTreeClassifier model
    model = DecisionTreeClassifier()
    # Train the model using the training data
    model.fit(X_train, y_train)
    # Make predictions on the validation data
    prediction = model.predict(X_val)
    # Print the accuracy score of the model rounded to 3 decimal places
    print(round(accuracy_score(y_val, prediction), 3))
