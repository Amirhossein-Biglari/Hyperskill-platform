def gini_impurity(labels: list):
    probabilities = [labels.count(label)/len(labels) for label in set(labels)]
    return 1 - sum([prob ** 2 for prob in probabilities])


def weighted_gini_impurity(node1_labels, node2_labels):
    n = len(node1_labels) + len(node2_labels)
    return len(node1_labels) / n * gini_impurity(node1_labels) + len(node2_labels) / n * gini_impurity(node2_labels)


print(gini_impurity(input().split()), weighted_gini_impurity(input().split(), input().split()))