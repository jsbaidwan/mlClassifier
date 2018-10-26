# import iris data set from scikit learn library

from sklearn.datasets import load_iris

iris = load_iris()

# features
print(iris.feature_names)

# labels
print(iris.target_names)

