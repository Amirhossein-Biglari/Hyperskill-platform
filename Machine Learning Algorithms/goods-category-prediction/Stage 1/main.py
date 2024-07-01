import pandas as pd
import nltk
import pickle
from nltk.tokenize import regexp_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords


nltk.download("stopwords")
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Make it a set because it is faster for searching!
stop_words = set(stopwords.words('english'))


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:

    def tokenize_text(text: str) -> list[str]:

        # Remove extraneous text
        text = (
            text.lower().replace("]", "").replace("[", "")
            .replace("\\n", "").replace("\\r\\n", "")
            .replace("^", "").replace("_", "")
            .replace("`", "").replace("\\", "").strip()
        )

        # Tokenize with regexp token with the pattern [A-z]+
        tokens = regexp_tokenize(text=text, pattern='[A-z]+')

        # Remove stopwords
        tokens = [token for token in tokens if token not in stop_words]

        return tokens

    def lemmatize_text(tokens: list[str]) -> list[str]:

        # Instantiate WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()

        # Generate POS tag for each word
        tokens = nltk.pos_tag(tokens)

        # Lemmatize with generated POS tags
        tokens = [lemmatizer.lemmatize(token, pos=f"{tag_map(tag)}") for token, tag in tokens]

        return tokens

    def tag_map(postag: str) -> str:
        if postag.startswith("J"):
            return wordnet.ADJ
        elif postag.startswith("V"):
            return wordnet.VERB
        elif postag.startswith(("R", "D", "P", "X")):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    # Add a column called `tokens` to the DataFrame containing the preprocessed data
    df["tokens"] = df["description"].apply(lambda x: lemmatize_text(tokenize_text(x)))

    return df


def main():

    # Load the data as a DataFrame
    df = pd.read_csv("../data/descriptions.csv")

    # Drop null values from DataFrame
    df = df.dropna()

    # Remove rows with extranoues values
    df = df = df[~(df.description.str.match(r'^[\s]+$|^[#]+$|^[-]+$|^\.$|^[0-9\s\-\.]+$|^\b(?:\w+\s*){1,2}\b$|No\. 30247: 3\/8"-24M'))]

    # Perform preprocessing
    preprocessed_data = preprocess_data(df)

    # Print the first four rows as shown in the example
    print(*preprocessed_data.tokens.tolist()[:4], sep="\n")

    # Save the preprocessed data as a pickle file to be used in later stages
    with open("../data/preprocessed_df.pkl", "wb") as f:
        pickle.dump(preprocessed_data, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()