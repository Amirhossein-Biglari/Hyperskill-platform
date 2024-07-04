# Word Semantics with Embeddings Vector

## Description
In this stage of the project, you will transform product descriptions into a machine-readable format using Word2Vec, a technique for generating word embeddings. These embeddings capture the contextual meanings of words, allowing product descriptions to be represented numerically for machine learning models.

```
def train_word2vec(train_data: pd.Series(list[str]), test_data: pd.Series(list[str])) -> \
        (KeyedVectors, pd.DataFrame, pd.DataFrame):

    # Instantiate the Word2Vec with the parameters
    w2v_model = Word2Vec(min_count=5, window=5, sg=0, vector_size=300, sample=6e-5, negative=20)

    # Build the vocabulary of w2v_model with the train_data
    ...

    """Train the w2v_model with the train_data,
    and the total_examples and epochs parameters.
    Set the epochs parameter to 15
    """
    w2v_model.train(..., total_examples=..., epochs=...)

    """Generate the train word embeddings vector and save as a DataFrame.
    Find the mean of the embeddings for each word. For words not in the vocabulary
    set the embeddings as a numpy array of zeros
    """
    train_df = pd.DataFrame([np.mean([w2v_model.wv[word] for word in tokens if word in w2v_model.wv]
                                     or [np.zeros(300)], axis=0) for tokens in train_data])

    """Generate the test word embeddings vector and save as a DataFrame.
    Find the mean of the embeddings for each word. For words not in the vocabulary
    set the embeddings as a numpy array of zeros
    """
    test_df = ...

    return w2v_model, train_df, test_df
```

After completing the tasks in the train_word2vec function, include the main function and run the program:

```
def main():

    # Load the preprocessed_df.pkl file from the data directory
    with open("../data/preprocessed_df.pkl", "rb") as f:
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
    print(sorted(model.wv.key_to_index.keys())[:50])

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
```

## Objectives
To complete this stage, you need to:

1. Finish the tasks in the `train_word2vec` function.
2. Run the `main` function to:
   - Load `preprocessed_df.pkl` from the data directory.
   - Split the data into train and test sets.
   - Get the labels and preprocessed tokens for the train and test sets.
   - Call the `train_word2vec` function.
   - Print a sorted list of the first 50 words in the Word2Vec vocabulary.
   - Save pickle files to the data directory.

Ensure to run your solution before pressing the Check button.
