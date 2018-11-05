
import numpy as np

# import iris data set from scikit learn library
from sklearn.datasets import load_iris

iris = load_iris()

# Remove one example of each type of flower by first storing it in test_index variable
test_index = [0, 50, 100]


# Training data
# removing three entries from the data and target variables
train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index, axis=0)
