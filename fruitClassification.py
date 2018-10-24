from sklearn import tree

features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
labels = ["apple", "apple", "orange", "orange"]

# Classifier for supervised learning
# Classifier is a box of rules
clf = tree.DecisionTreeClassifier()

# Find patterns in the training data
# Training algorithm is included in the classifier object is called Fit
clf = clf.fit(features, labels)





