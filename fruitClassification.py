from sklearn import tree

features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
labels = ["apple", "apple", "orange", "orange"]

# Classifier for supervised learning
clf = tree.DecisionTreeClassifier()
