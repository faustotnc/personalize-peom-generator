# Setting up PlaidML Backend
import plaidml.keras
import os
plaidml.keras.install_backend()
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import keras
import keras.backend as k
from tensorflow.keras import layers


# The size of th


class PoemModel:

    def __init__(self, vocab_size, hidden_size, output_size, n_layers=1):

        self.model = keras.Sequential([
            layers.Embedding(47 * 3, 47 * 3),
            layers.GRU(47 * 3, )
        ])
