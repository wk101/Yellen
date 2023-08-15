import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Flatten, Reshape, Input
from tensorflow.keras.models import Sequential, Model

# Load and preprocess the data
df = pd.read_csv("forex_data.csv")
data = df["EUR/USD"].values

# Normalize data
data = (data - np.mean(data)) / np.std(data)

def sliding_window(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

window_size = 5
X, y = sliding_window(data, window_size)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Generator
def build_generator():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(window_size, 1)))
    model.add(LSTM(50, return_sequences=True))
    model.add(Flatten())
    model.add(Dense(1))
    return model

# Discriminator
def build_discriminator():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(window_size + 1, 1)))
    model.add(LSTM(50))
    model.add(Dense(1, activation='sigmoid'))
    return model

generator = build_generator()
discriminator = build_discriminator()

# Compile discriminator
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# GAN
z = Input(shape=(window_size, 1))
currency_pair = generator(z)

# The discriminator takes the generated data and the real data
combined_data = tf.concat([z, tf.reshape(currency_pair, (-1, 1, 1))], axis=1)
validity = discriminator(combined_data)

discriminator.trainable = False
gan = Model(z, validity)
gan.compile(loss='binary_crossentropy', optimizer='adam')

# Train
epochs = 10000
batch_size = 32

real_labels = np.ones((batch_size, 1))
fake_labels = np.zeros((batch_size, 1))

for epoch in range(epochs):
    
    # Training discriminator
    idx = np.random.randint(0, X.shape[0], batch_size)
    real_pairs = X[idx]
    real_prices = y[idx].reshape(-1, 1, 1)
    
    # Generate a batch of new currency pairs
    noise = np.random.normal(0, 1, (batch_size, window_size, 1))
    gen_prices = generator.predict(noise)
    gen_data = np.concatenate([noise, gen_prices], axis=1)

    d_loss_real = discriminator.train_on_batch(np.concatenate([real_pairs, real_prices], axis=1), real_labels)
    d_loss_fake = discriminator.train_on_batch(gen_data, fake_labels)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    # Training generator
    noise = np.random.normal(0, 1, (batch_size, window_size, 1))
    g_loss = gan.train_on_batch(noise, real_labels)
    
    print(f"{epoch}/{epochs} [D loss: {d_loss[0]} | D accuracy: {100 * d_loss[1]}] [G loss: {g_loss}]")
