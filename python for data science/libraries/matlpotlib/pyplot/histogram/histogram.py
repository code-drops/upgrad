# A histogram is a frequency chart that records the occurrence of an entry or an element in a data set.

import numpy as np
import matplotlib.pyplot as plt

# data
age = np.array([23, 22, 24, 24, 23, 23, 22, 23, 24, 24, 24, 22, 24, 23, 24, 23, 22, 24, 23, 23, 22, 23, 23, 24, 23, 24, 23, 22, 24, 22, 23, 24, 23, 24, 22, 22, 24, 23, 22, 24, 24, 24, 23, 24, 24, 22, 23, 23, 24, 22, 22, 24, 22, 23, 22, 23, 22, 23, 23, 23, 23, 22, 22, 23, 23, 23, 23, 23, 23, 22, 29, 29, 27, 28, 28, 29, 28, 27, 26, 27, 28, 29, 26, 28, 26, 28, 27, 27, 28, 28, 26, 29, 28, 28, 26, 27, 26, 28, 27, 29, 29, 27, 27, 27, 28, 29, 29, 29, 27, 28, 28, 26, 28, 27, 26, 26, 27, 26, 29, 28, 28, 28, 29, 26, 26, 26, 29, 26, 28, 26, 28, 28, 27, 27, 27, 29, 27, 28, 27, 26, 29, 29, 27, 29, 26, 29, 26, 29, 29, 27, 28, 28, 27, 29, 26, 28, 26, 28, 27, 29, 29, 29, 27, 27, 29, 29, 26, 26, 26, 27, 28, 27, 28, 28, 29, 27, 26, 27, 29, 28, 29, 27, 27, 26, 26, 26, 26, 29, 28, 28, 33, 34, 33, 33, 34, 33, 31, 32, 33, 33, 32, 34, 32, 31, 33, 34, 31, 33, 34, 33, 34, 33, 32, 33, 31, 33, 32, 32, 31, 34, 33, 31, 34, 32, 32, 31, 32, 31, 32, 34, 33, 33, 31, 32, 32, 31, 32, 33, 34, 32, 34, 31, 32, 31, 33, 32, 34, 31, 32, 34, 31, 31, 34, 34, 34, 32, 34, 33, 33, 32, 32, 33, 31, 33, 31, 32, 34, 32, 32, 31, 34, 32, 32, 31, 32, 34, 32, 33, 31, 34, 31, 31, 32, 31, 33, 34, 34, 34, 31, 33, 34, 33, 34, 31, 34, 34, 33, 31, 32, 33, 31, 31, 33, 32, 34, 32, 34, 31, 31, 34, 32, 32, 31, 31, 32, 31, 31, 32, 33, 32, 31, 32, 32, 31, 31, 34, 31, 34, 33, 32, 31, 34, 34, 31, 34, 31, 32, 34, 33, 33, 34, 32, 33, 31, 31, 33, 32, 31, 31, 31, 37, 38, 37, 37, 36, 37, 36, 39, 37, 39, 37, 39, 38, 36, 37, 36, 38, 38, 36, 39, 39, 37, 39, 36, 37, 36, 36, 37, 38, 36, 38, 39, 39, 36, 38, 37, 39, 38, 39, 39, 36, 38, 37, 38, 39, 36, 37, 36, 36, 38, 38, 38, 39, 36, 37, 37, 39, 37, 37, 36, 36, 39, 37, 36, 36, 36, 39, 37, 37, 37, 37, 39, 36, 39, 37, 38, 37, 36, 36, 39, 39, 36, 36, 39, 39, 39, 37, 38, 36, 36, 37, 38, 37, 38, 37, 39, 39, 37, 39, 36, 36, 39, 39, 39, 36, 38, 39, 39, 39, 39, 38, 36, 37, 37, 38, 38, 39, 36, 37, 37, 39, 36, 37, 37, 36, 36, 36, 38, 39, 38, 36, 38, 36, 39, 38, 36, 36, 37, 39, 39, 37, 37, 37, 36, 37, 36, 36, 38, 38, 39, 36, 39, 36, 37, 37, 39, 39, 36, 38, 39, 39, 39, 37, 37, 37, 37, 39, 36, 37, 39, 38, 39, 36, 37, 38, 39, 38, 36, 37, 38, 42, 43, 44, 43, 41, 42, 41, 41, 42, 41, 43, 44, 43, 44, 44, 42, 43, 44, 43, 41, 44, 42, 43, 42, 42, 44, 43, 42, 41, 42, 41, 41, 41, 44, 44, 44, 41, 43, 42, 42, 43, 43, 44, 44, 44, 44, 44, 41, 42, 44, 43, 42, 42, 43, 44, 44, 44, 44, 41, 42, 43, 43, 43, 41, 43, 41, 42, 41, 42, 42, 41, 42, 44, 41, 43, 42, 41, 43, 41, 44, 44, 43, 43, 43, 41, 41, 41, 42, 43, 42, 48, 48, 48, 49, 47, 45, 46, 49, 46, 49, 49, 46, 47, 45, 47, 45, 47, 49, 47, 46, 46, 47, 45, 49, 49, 49, 45, 46, 47, 46, 45, 46, 45, 48, 48, 45, 49, 46, 48, 49, 47, 48, 45, 48, 46, 45, 48, 45, 46, 46, 48, 47, 46, 45, 48, 46, 49, 47, 46, 49, 48, 46, 47, 47, 46, 48, 47, 46, 46, 49, 50, 54, 53, 55, 51, 50, 51, 54, 54, 53, 53, 51, 51, 50, 54, 51, 51, 55, 50, 51, 50, 50, 53, 52, 54, 53, 55, 52, 52, 50, 52, 55, 54, 50, 50, 55, 52, 54, 52, 54])

# bins represents the number of bars on histogram(default_valuue = 10)
plt.hist(age,bins=5,edgecolor="red",color="yellow")
plt.show()

# represents the data within defined range
plt.hist(age, bins=4, range=[20, 60], edgecolor='white')
plt.show()