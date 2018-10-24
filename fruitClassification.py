from sklearn import tree


features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
labels = ["apple", "apple", "orange", "orange"]

# Classifier for supervised learning
# Classifier is a box of rules
clf = tree.DecisionTreeClassifier()

# Find patterns in the training data
# Training algorithm is included in the classifier object is called Fit
clf = clf.fit(features, labels)
# clf is now a trained classifier


# Classifier notice oranges tends to weigh more, so it'll crate a rule that the heavier
# fruit is, more likely it is to be orange

prediction = clf.predict([150, "bumpy"])






