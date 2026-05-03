import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dataset (XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)   # make y 2D for sigmoid output

# MLP Model
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(X, y, epochs=1000, verbose=0)
print("Training completed")

# Evaluate model
loss, acc = model.evaluate(X, y, verbose=0)
print("Final Loss:", loss)
print("Final Accuracy:", acc)

# Predictions
pred = model.predict(X)
print("Predictions:")
print(pred)

# Show plots
plt.plot(history.history['loss'])
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.show()
