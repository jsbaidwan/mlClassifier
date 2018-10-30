# import iris data set from scikit learn library

from sklearn.datasets import load_iris

iris = load_iris()

# features
print(iris.feature_names)

# labels
print(iris.target_names)

# first entry in the iris data set
print(iris.data[0])

#
print(iris.target[0])

# print entire Iris dataset
for i in range(len(iris.target)):
    print("Example %d: label %s, feature %s" % (i, iris.target[i], iris.data[i]))


