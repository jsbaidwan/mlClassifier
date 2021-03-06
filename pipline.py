from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

import random
class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        best_dist = euc(row, self.X_train[0])
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

# How to test a model and determine accuracy

# Partition data into 2 sets, train and test

# import a dataset
from sklearn import datasets

iris = datasets.load_iris()

# Can think of classifier as a function f(x) = y
X = iris.data  # features
y = iris.target  # labels

# partition into training and testing sets
from sklearn.model_selection import train_test_split

# test_size=0.5 -> split in half
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Classifier
# from sklearn.neighbors import KNeighborsClassifier

# my_classifier = KNeighborsClassifier()
my_classifier = ScrappyKNN()
my_classifier.fit(X_train, y_train)

# Predict
predictions = my_classifier.predict(X_test)
print(predictions)

# Test
from sklearn.metrics import accuracy_score
print(accuracy_score(predictions, y_test))

# # Repeat using KNN
# # Classifier
# from sklearn.neighbors import KNeighborsClassifier
#
# my_classifier = KNeighborsClassifier()
# my_classifier.fit(X_train, y_train)
#
# # predict
# predictions = my_classifier.predict(X_test)
# print(predictions)
#
# # test
# from sklearn.metrics import accuracy_score
#
# # print the predication
# print(accuracy_score(predictions, y_test))


