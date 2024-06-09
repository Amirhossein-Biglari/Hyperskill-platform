import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from collections import Counter
from tqdm import tqdm


np.random.seed(52)


def convert_embarked(x):
    if x == 'S':
        return 0
    elif x == 'C':
        return 1
    else:
        return 2


def create_bootstrap(_data):
    # np.random.choice(5, size=3) is the same as np.random.randint(5, size=3)
    return np.random.choice(_data.shape[0], replace=True, size=_data.shape[0])


class RandomForestClassifier:
    def __init__(self, n_trees=10, max_depth=np.iinfo(np.int64).max, min_error=1e-6):

        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_error = min_error

        self.is_fit = False

    def fit(self, X_train, y_train):

        self.forest = []

        for i in (range(self.n_trees)):
            model = DecisionTreeClassifier(
                max_depth=self.max_depth,
                min_impurity_decrease=self.min_error,
                max_features='sqrt')
            indices = create_bootstrap(y_train)
            model.fit(X_train[indices], y_train[indices])
            self.forest.append(model)

        self.is_fit = True

    def predict(self, X_test):

        if not self.is_fit:
            raise AttributeError('The forest is not fit yet! Consider calling .fit()')

        # models_prediction = []
        # for model in self.forest:
        #     models_prediction.append(model.predict(X_test))
        #
        # models_prediction = np.array(models_prediction)
        #
        # final_predictions = []
        # for i in range(X_test.shape[0]):
        #     counter = Counter(models_prediction[:, i])
        #     final_predictions.append(counter.most_common(1)[0][0])
        #
        # return final_predictions

        predictions = np.zeros(shape=X_test.shape[0])

        for model in self.forest:
            predictions += model.predict(X_test)

        return np.round(predictions / len(self.forest))


if __name__ == '__main__':

    data = pd.read_csv('https://www.dropbox.com/s/4vu5j6ahk2j3ypk/titanic_train.csv?dl=1')

    data.drop(
        ['PassengerId', 'Name', 'Ticket', 'Cabin'],
        axis=1,
        inplace=True
    )
    data.dropna(inplace=True)

    # Separate these back
    y = data['Survived'].astype(int)
    X = data.drop('Survived', axis=1)

    X['Sex'] = X['Sex'].apply(lambda x: 0 if x == 'male' else 1)
    X['Embarked'] = X['Embarked'].apply(lambda x: convert_embarked(x))

    X_train, X_val, y_train, y_val = \
        train_test_split(X.values, y.values, stratify=y, train_size=0.8)

    # Make your code here...
    results = []
    for i in range(1, 21):
        random_forest = RandomForestClassifier(n_trees=i)
        random_forest.fit(X_train, y_train)
        y_pred = random_forest.predict(X_val)
        accuracy = round(accuracy_score(y_val, y_pred), 3)
        results.append(accuracy)

    print(results)