# Good features are informative, independent, and simple. We'll introduce these concepts by using a histogram to
# visualize a feature from a toy dataset.

import numpy as np
import matplotlib.pyplot as plt

# Creating a population of thousand dogs

greyhounds = 500
labs = 500

# Assume greyhounds are normally 28" tall
# Assume labradors are normally 24" tall
# Assume normal distribution of +/- 4"
grey_height = 28 + 4 * np.random.rand(greyhounds)
lab_height = 24 + 4 * np.random.rand(labs)

# Two arrays of numbers and we can visualize them in a histogram
# Greyhounds - red, labradors - blue
plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()

# Independent features are best
# Avoid redundant features (height in in AND height in cm)

# Ideal features are:
# Informative
# Independent
# Simple

