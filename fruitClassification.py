from sklearn import tree

# Store are list in the features variable consists of [weight, texture]
features = [[140, 0], [130, 0], [150, 1], [170, 1]]

labels = ["apple", "apple", "orange", "orange"]

target_names = ["Apple", "orange"]
features_name = ["weight", "texture"]

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


# Generating visualization
from sklearn.externals.six import StringIO
import pydot
from IPython.display import Image
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                    feature_names=features_name,
                    class_names=target_names,
                    filled=True, rounded=True,
                    impurity=False)
graph  = pydot.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
graph.write_pdf('fruit.pdf')





