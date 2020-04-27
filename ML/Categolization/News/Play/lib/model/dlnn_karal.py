import tensorflow as tf
from tensorflow import keras
from dataclasses import dataclass as dc
import numpy as np
# import matplotlib.pyplot as plt

@dc
class Dlnn:
    def __model_init__(self):
        print('\nTensorflow: Instantiation')

    def set_model(self, n_inputs, units, catetories):
        self.model = keras.Sequential([
            # keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(units, input_dim=n_inputs, activation='relu'),
            keras.layers.Dense(units, activation='relu'),
            keras.layers.Dense(catetories, activation='softmax')
        ])
        self.compile_model()

    def compile_model(self):
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])
        print('Model Compiled.')

    def fit(self, inputs, labels, epochs=10):
        history = self.model.fit(inputs, labels, epochs=epochs)
        print('\nhistory dict:', history.history)

    def evaluate_model(self, inputs, labels, verbose=2):
        test_loss, test_acc = self.model.evaluate(inputs, labels, verbose=verbose)
        print('\nTest accuracy:', test_acc)

    def predict(self, tests_inputs, answers):
        probability_model = tf.keras.Sequential([self.model, tf.keras.layers.Softmax()])
        predictions = probability_model.predict(tests_inputs)
        for p, a in zip(predictions, answers):
            print("Prediction:",np.argmax(p), ", Answer:", np.argmax(a))