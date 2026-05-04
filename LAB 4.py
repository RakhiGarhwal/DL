import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense

# Dummy data
X = np.random.rand(100, 10, 1)
y = np.random.rand(100, 1)

def build_model(model_type):
    model = Sequential()

    if model_type == "RNN":
        model.add(SimpleRNN(32, input_shape=(10,1)))
    elif model_type == "LSTM":
        model.add(LSTM(32, input_shape=(10,1)))
    else:
        model.add(GRU(32, input_shape=(10,1)))

    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

for t in ["RNN", "LSTM", "GRU"]:
    print(f"\nTraining {t}")
    model = build_model(t)
    model.fit(X, y, epochs=1)