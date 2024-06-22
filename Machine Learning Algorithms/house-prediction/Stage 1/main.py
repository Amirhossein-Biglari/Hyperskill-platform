import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("house_class.csv")

    print(df.shape[0])
    print(df.shape[1])
    print(df.isnull().any().any())
    print(df.Room.max())
    print(df.Area.mean())
    print(df.Zip_loc.nunique())
