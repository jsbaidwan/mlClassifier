import numpy as np
import matplotlib.pyplot as plt

#Creating a population of thousand dogs

greyhounds = 500
labs = 500

# Give height to each dog
grey_height = 28 + 4 * np.random.rand(greyhounds)
lab_height = 24 + 4 * np.random.rand(labs)