from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras import metrics
import tensorflow_addons as tfa


def init_vanilla_nn(n_neurons, input_dim, output_dim):
    model = Sequential()
    model.add(
        layers.Dense(n_neurons[0], activation='relu', input_dim=input_dim))
    for i in range(1, len(n_neurons)):
        model.add(layers.Dense(n_neurons[i], activation='relu'))
    model.add(layers.Dense(output_dim, activation='linear'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae', 'mse', 'mape', tfa.metrics.R, metrics.MeanRelativeError])

    return model
