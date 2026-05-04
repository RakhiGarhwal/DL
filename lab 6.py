import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sentence = ["I", "love", "AI"]
weights = np.array([0.2, 0.5, 0.3])

weights = weights / weights.sum()

sns.heatmap([weights], annot=True, xticklabels=sentence)
plt.show()