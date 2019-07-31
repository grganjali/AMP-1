import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.datasets import make_blobs

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.ylim(-3,3)
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show(plt.plot(X, y, 'o'))
