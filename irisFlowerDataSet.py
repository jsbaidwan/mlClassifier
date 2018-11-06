
import numpy as np

# import iris data set from scikit learn library
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

# Remove one example of each type of flower by first storing it in test_index variable
test_index = [0, 50, 100]


# Training data
# removing three entries from the data and target variables
train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index, axis=0)

# Testing Data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

clf = tree.DecisionTreeClassifier()
# fit(features, labels)
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))
