# Word Semantics with Embeddings Vector

## Description

In this project, we transform product descriptions into a machine-readable format using Word2Vec, a popular technique for generating word embeddings. These embeddings capture the contextual meanings of words, allowing us to represent product descriptions in a numerical format suitable for machine learning models.

### Function: train_word2vec

The `train_word2vec` function performs the following tasks:

- Instantiates the Word2Vec model with specific parameters.
- Builds the vocabulary with the training data.
- Trains the Word2Vec model.
- Generates the training word embeddings vector.
- Generates the test word embeddings vector.

### Main Function

The `main` function performs the following tasks:

- Loads the preprocessed DataFrame.
- Splits the data into train and test sets.
- Gets the labels for the train and test sets.
- Gets the preprocessed tokens.
- Calls the `train_word2vec` function.
- Prints the first 50 words of the sorted vocabulary.
- Saves the generated data and model as pickle files.

## Objectives

To complete this stage:

1. Finish the tasks in the `train_word2vec` function.
2. Run the `main` function to:
   - Load `preprocessed_df.pkl` from the data directory.
   - Split the data into train and test sets.
   - Get the labels and preprocessed tokens for the train and test sets.
   - Call the `train_word2vec` function.
   - Print a sorted list of the first 50 words in the Word2Vec vocabulary.
   - Save the resulting data and model as pickle files in the data directory.

Before pressing the Check button, please run your solution.
