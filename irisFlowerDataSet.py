# import iris data set from scikit learn library

from sklearn.datasets import load_iris

iris = load_iris()

# Remove one example of each type of flower by first storing it in test_index variable
test_index = [0, 50, 100]

