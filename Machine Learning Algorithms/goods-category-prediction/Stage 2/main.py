import pandas as pd
import numpy as np
import nltk
import pickle
from nltk.tokenize import regexp_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.model_selection import train_test_split


def train_word2vec(train_data: pd.Series, test_data: pd.Series) -> \
            tuple[KeyedVectors, pd.DataFrame, pd.DataFrame]:

    # Instantiate the Word2Vec with the parameters
    w2v_model = Word2Vec(min_count=5, window=5, sg=0, vector_size=300, sample=6e-5, negative=20)

    # Build the vocabulary of w2v_model with the train_data
    w2v_model.build_vocab(train_data)

    """Train the w2v_model with the train_data,
    and the total_examples and epochs parameters.
    Set the epochs parameter to 15
    """
    w2v_model.train(train_data, total_examples=w2v_model.corpus_count, epochs=15)

    """Generate the train word embeddings vector and save as a DataFrame.
    Find the mean of the embeddings for each word. For words not in the vocabulary
    set the embeddings as a numpy array of zeros
    """
    train_df = pd.DataFrame(
        [np.mean([w2v_model.wv[word] for word in tokens if word in w2v_model.wv] or [np.zeros(300)], axis=0) for tokens in train_data]
    )

    """Generate the test word embeddings vector and save as a DataFrame.
    Find the mean of the embeddings for each word. For words not in the vocabulary
    set the embeddings as a numpy array of zeros
    """
    test_df = pd.DataFrame(
        [np.mean([w2v_model.wv[word] for word in tokens if word in w2v_model.wv] or [np.zeros(300)], axis=0) for tokens in train_data]
    )

    return w2v_model, train_df, test_df


def main():

    # Load the preprocessed_df.pkl file from the data directory
    with open("preprocessed_df.pkl", "rb") as f:
        df = pickle.load(f)

    # split the preproceesed data into train and test sets
    train, test = train_test_split(df, test_size=.1, random_state=10, stratify=df.categories)

    # Get the categories for the train and test sets
    train_labels = train.categories
    test_labels = test.categories

    # Get the preprocessed tokens from the train and test sets
    train_tokens = train.tokens
    test_tokens = test.tokens

    # Call the tain_word2vec function
    w2v_model, train_df, test_df = train_word2vec(train_tokens, test_tokens)

    # Sort the vocabulary generated from the word2vec model and print first 50 words
    print(sorted(w2v_model.wv.key_to_index.keys())[:50])

    # Save the following as pickle files in the data directory
    with open('../data/w2v_model.pkl', 'wb') as f:
        pickle.dump(w2v_model, f, pickle.HIGHEST_PROTOCOL)

    with open('../data/train_df.pkl', 'wb') as f:
        pickle.dump(train_df, f, pickle.HIGHEST_PROTOCOL)

    with open('../data/test_df.pkl', 'wb') as f:
        pickle.dump(test_df, f, pickle.HIGHEST_PROTOCOL)

    with open('../data/train_labels.pkl', 'wb') as f:
        pickle.dump(train_labels, f, pickle.HIGHEST_PROTOCOL)

    with open('../data/test_labels.pkl', 'wb') as f:
        pickle.dump(test_labels, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
    # print("""['aa', 'aaa', 'aab', 'aac', 'aaw', 'aax', 'ab', 'aba', 'abacus', 'abalone', 'abandon', 'abb', 'abbey', 'abbreviation', 'abc', 'abdomen', 'abdominal', 'abeb', 'ability', 'ablative', 'able', 'ably', 'abound', 'abraham', 'abrasion', 'abrasive', 'abroad', 'abruptly', 'abs', 'absence', 'absolute', 'absolutely', 'absorb', 'absorbable', 'absorbed', 'absorbency', 'absorbent', 'absorber', 'absorbs', 'absorption', 'abstract', 'abundance', 'abundant', 'abuse', 'ac', 'acacia', 'academic', 'academy', 'acai', 'acamps']""")