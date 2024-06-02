import pandas as pd


class Node:
    def __init__(self):
        # Initialize a node in the decision tree
        self.left = None
        self.right = None
        self.term = False  # Indicates if the node is a terminal (leaf) node
        self.label = None  # Label for terminal nodes
        self.feature = None  # Feature used for splitting
        self.value = None  # Value of the feature used for splitting

    def set_split(self, feature, value):
        # Set the feature and its value for splitting at this node
        self.feature = feature
        self.value = value

    def set_term(self, label):
        # Set the node as terminal and assign its label
        self.term = True
        self.label = label


class DecisionTree:
    def __init__(self, node) -> None:
        # Initialize the decision tree with a root node
        self.root = node
        self.minimum_num_samples = 1  # Minimum number of samples to split a node

    def _gini_impurity(self, labels: list):
        """
        Calculate the Gini impurity for a list of labels.

        Gini impurity measures the likelihood of an incorrect classification
        of a new instance of a random variable. It reaches its minimum (zero) 
        when all cases in a node fall into a single target category.

        Args:
            labels (list): A list of labels.

        Returns:
            float: The Gini impurity of the labels.
        """
        # Calculate the probability of each unique label
        probabilities = [labels.count(label) / len(labels) for label in set(labels)]
        # Calculate the Gini impurity
        return 1 - sum([prob ** 2 for prob in probabilities])

    def _weighted_gini_impurity(self, node1_labels: list, node2_labels: list):
        """
        Calculate the weighted Gini impurity for two sets of labels.

        The weighted Gini impurity takes into account the size of each node
        and combines their Gini impurities to give an overall measure.

        Args:
            node1_labels (list): A list of labels for the first node.
            node2_labels (list): A list of labels for the second node.

        Returns:
            float: The weighted Gini impurity of the two nodes.
        """
        # Total number of labels
        n = len(node1_labels) + len(node2_labels)
        # Calculate the weighted Gini impurity
        return (len(node1_labels) / n * self._gini_impurity(node1_labels) +
                len(node2_labels) / n * self._gini_impurity(node2_labels))

    def _split_function(self, dataset: pd.DataFrame, labels: pd.Series):
        """
        Find the best feature and value to split the dataset based on Gini impurity.

        This function iterates over all features and their unique values to find
        the split that results in the lowest weighted Gini impurity.

        Args:
            dataset (pd.DataFrame): DataFrame containing the feature columns.
            labels (pd.Series): Series containing the labels.

        Returns:
            tuple: Minimum weighted Gini impurity, best feature to split on, 
                value of the best feature to split on, indices of left and right nodes.
        """
        minimum_weighted_gini = 1  # Initialize with a value higher than maximum Gini impurity
        best_feature = None  # To store the best feature found
        best_feature_value = None  # To store the best value of the feature found
        best_left_node_index = None  # To store the indices of the left node
        best_right_node_index = None  # To store the indices of the right node

        # Iterate over each feature in the DataFrame
        for feature in dataset.columns:
            # Iterate over each unique value in the feature
            for value in dataset[feature].unique():
                # Get the indices of the left and right nodes based on the feature value
                left_node_index = dataset[dataset[feature] == value].index
                right_node_index = dataset[dataset[feature] != value].index

                # Calculate the weighted Gini impurity for the split
                weighted_gini = self._weighted_gini_impurity(labels[left_node_index].values.tolist(),
                                                            labels[right_node_index].values.tolist())

                # Update the best split if a lower weighted Gini impurity is found
                if weighted_gini < minimum_weighted_gini:
                    minimum_weighted_gini = weighted_gini
                    best_feature = feature
                    best_feature_value = value
                    best_left_node_index = left_node_index.tolist()
                    best_right_node_index = right_node_index.tolist()

        # Return the results of the best split found
        return minimum_weighted_gini, best_feature, best_feature_value, best_left_node_index, best_right_node_index

    def _recursive_split_function(self, dataset: pd.DataFrame, labels: pd.Series, node):
        """
        Recursively split the dataset to build a decision tree.

        This function splits the dataset using the best feature and value, and 
        recursively applies the same process to the resulting child nodes.

        Args:
            dataset (pd.DataFrame): DataFrame containing the feature columns.
            labels (pd.Series): Series containing the labels.
            node (Node): Current node in the decision tree.
        """
        # Calculate the Gini impurity for the current set of labels
        gini = self._gini_impurity(labels.values.tolist())

        # Drop duplicates to avoid redundant splits
        d = dataset.drop_duplicates()
        l = len(d)

        # Check for terminal condition: no impurity, minimum samples, or only one unique sample
        if gini == 0 or len(dataset) <= self.minimum_num_samples or l == 1:
            label = labels.mode()[0]  # Assign the most frequent label
            node.set_term(label)  # Mark the node as terminal
            return

        # Find the best split for the current node
        minimum_wg, feature, value, left_node_index, right_node_index = self._split_function(dataset, labels)

        # Set the split feature and value for the current node
        node.set_split(feature, value)
        print(f'Made split {feature} with value {value}')  # Print the split information

        # Recursively split the left node
        left = Node()
        node.left = left
        self._recursive_split_function(dataset.loc[left_node_index], labels.loc[left_node_index], left)

        # Recursively split the right node
        right = Node()
        node.right = right
        self._recursive_split_function(dataset.loc[right_node_index], labels.loc[right_node_index], right)

    def fit(self, dataset: pd.DataFrame):
        """
        Build a decision tree classifier from the training dataset.

        This function initiates the recursive process of splitting the dataset
        to build the decision tree, starting from the root node.

        Args:
            dataset (pd.DataFrame): DataFrame containing the training data with 
                                    features and labels.
        """
        # Separate features (X) and labels (y) from the dataset
        X = dataset.drop(columns='Survived')
        y = dataset['Survived']
        # Start the recursive splitting process from the root node
        self._recursive_split_function(X, y, self.root)


# Load dataset from CSV file
df = pd.read_csv('data_stage4.csv', index_col='Unnamed: 0')
# Initialize the decision tree with a root node
ds = DecisionTree(Node())
# Fit the decision tree with the dataset
ds.fit(df)