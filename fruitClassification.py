from sklearn import tree

# Store are list in the features variable consists of [weight, texture]
features = [[140, 0], [130, 0], [150, 1], [170, 1]]

labels = ["apple", "apple", "orange", "orange"]

# Classifier for supervised learning
# Classifier is a box of rules
# clf will store our DecisionTree classifier
clf = tree.DecisionTreeClassifier()

# Find patterns in the training data
# Training algorithm is included in the classifier object is called Fit
# Fit method trains the decision tree on our data set
clf = clf.fit(features, labels)
# clf is now a trained classifier


# Classifier notice oranges tends to weigh more, so it'll crate a rule that the heavier
# fruit is, more likely it is to be orange

prediction = clf.predict([[150, 0]])

# print the output
print(prediction)








