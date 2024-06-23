import pandas as pd
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    df = pd.read_csv("house_class.csv")

    X = df.drop('Price', axis=1)
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1, stratify=X['Zip_loc'].values)

    print(X_train.Zip_loc.value_counts().to_dict())
