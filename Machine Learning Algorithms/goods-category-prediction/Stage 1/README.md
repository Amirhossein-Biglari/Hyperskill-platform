# Taming Textual Chaos

## Description
Imagine yourself browsing a massive retail marketplace with millions of products vying for your attention. You want a specific item but it feels like searching for a needle in a haystack. This struggle is common to shoppers and retailers. Shoppers waste time searching through things they don't need, while sellers struggle to make their products discoverable.

In this project, you'll tackle the challenge of product discoverability by building a system that automatically categorizes products based on their descriptions. You will use the Retail Products Classification dataset, which contains thousands of retail product descriptions categorized into 21 distinct categories. This dataset will serve as the foundation for training your machine learning model to learn the key features that differentiate products across different categories.

## Objectives
To complete this stage:
1. Download the `description.csv` file and save it in the data directory.
2. Remove extraneous rows and texts.
3. Complete the inner functions: `tokenize_text` and `lemmatize_text`.
4. Run the main function to:
   - Load `description.csv` as a pandas DataFrame and drop null values.
   - Remove extraneous rows from the DataFrame.
   - Perform the preprocessing operation.
   - Print the preprocessed data.
   - Save the preprocessed data as a `preprocessed_df.pkl` file in the data directory.

## Data Preprocessing
Prepare the product descriptions for the machine learning model by applying several text preprocessing techniques:

1. **Cleaning the Text:**
   - Convert text to lowercase.
   - Remove extraneous characters such as `]`, `[`, `\\n`, `\\r\\n`, `^`, `_`, `\``, and `\\`.
   - Strip leading and trailing spaces.

2. **Tokenizing and Lemmatizing:**
   - Download necessary NLTK resources: stopwords, wordnet, and averaged_perceptron_tagger.
   - Tokenize the text using a regular expression pattern to extract words.
   - Remove stopwords from the tokenized text.
   - Lemmatize the tokens with Part-of-Speech tags mapped to appropriate WordNet POS tags.

## Main Function Workflow
1. Load the data from `description.csv` as a pandas DataFrame.
2. Drop null values from the DataFrame.
3. Remove rows with extraneous values using regular expressions to filter out irrelevant text.
4. Perform the text preprocessing (cleaning, tokenizing, lemmatizing) on the product descriptions.
5. Print the first few rows of the preprocessed data to verify the results.
6. Save the preprocessed DataFrame as `preprocessed_df.pkl` in the data directory.
