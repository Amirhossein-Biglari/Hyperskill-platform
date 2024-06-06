import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from collections import Counter
from tqdm import tqdm

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

# Function to create bootstrap samples
def create_bootstrap(_data):
    return np.random.choice(_data.shape[0], replace=True, size=_data.shape[0])

class RandomForestClassifier():
    def __init__(self, n_trees=10, max_depth=np.iinfo(np.int64).max, min_error=1e-6):
        # Initialize RandomForestClassifier with the given parameters
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_error = min_error
        self.is_fit = False

    def fit(self, X_train, y_train):
        # Fit the random forest to the training data
        self.forest = []

        for i in tqdm(range(self.n_trees)):
            # Create a decision tree with 'sqrt' feature selection
            model = DecisionTreeClassifier(max_features='sqrt')
            # Create bootstrap sample indices
            indices = create_bootstrap(y_train)
            # Fit the model on the bootstrap sample
            model.fit(X_train[indices], y_train[indices])
            # Add the trained model to the forest
            self.forest.append(model)

        self.is_fit = True

    def predict(self, X_test):
        # Predict using the random forest
        if not self.is_fit:
            raise AttributeError('The forest is not fit yet! Consider calling .fit()')

        # Use the first tree in the forest for prediction
        model = self.forest[0]
        return model.predict(X_test)

if __name__ == '__main__':
    # Read the Titanic dataset from CSV file
    data = pd.read_csv('titanic.csv')

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

    # Split the data into training and validation sets, maintaining the distribution of the target variable
    X_train, X_val, y_train, y_val = train_test_split(X.values, y.values, stratify=y, train_size=0.8)
    
    # Initialize and train the RandomForestClassifier
    random_forest = RandomForestClassifier()
    random_forest.fit(X_train, y_train)
    
    # Predict on the validation set
    y_pred = random_forest.predict(X_val)
    
    # Calculate and print the accuracy
    print(round(accuracy_score(y_val, y_pred), 3))
