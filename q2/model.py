import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint

is_load = 1

if is_load == 0:
    # prepare training datas
    print("Preparing training data")
    X_train = []
    Y_train = []

    for i in range(1000):
        for j in range(1000):
            X_train.append([i * 0.01, j * 0.01])
            Y_train.append([i * j * 0.0001])

    print("Preparing test data")
    X_test = []
    Y_test = []

    for i in range(900,1100):
        for j in range(1000):
            X_test.append([i * 0.01, j * 0.01])
            Y_test.append([i * j * 0.0001])

    print("Preparing validation data")
    X_val = []
    Y_val = []

    for i in range(1000,1200):
        for j in range(1000):
            X_val.append([i * 0.01, j * 0.01])
            Y_val.append([i * j * 0.0001])

def create_model():
    print("Creating model")
    model = keras.Sequential()
 
    model.add(keras.layers.Flatten(input_shape=(2,)))
    model.add(keras.layers.Dense(32, activation=tf.nn.relu))
    model.add(keras.layers.Dense(64, activation=tf.nn.relu))
    model.add(keras.layers.Dense(32, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1))

    model.compile(optimizer='adam',
            loss='mse',
            metrics=['mae'])

    return model

checkpoint_path = "training_1/model.ckpt"

def save_checkpoint():
    print("Saving model")
    cp_callback = ModelCheckpoint(filepath=checkpoint_path,
            save_weights_only=True,
            verbose=1)

    return cp_callback

model = create_model()
if(is_load):
    model.load_weights(checkpoint_path)
else:
    cb_1 = save_checkpoint()
    print("Fitting model")
    model.fit(X_train, Y_train, epochs=10, batch_size=1,
            validation_data=(X_val, Y_val),
            callbacks=[cb_1])

    print("Evaluating model")
    test_loss, test_acc = model.evaluate(X_test, Y_test)
    print("Test acc: ", test_acc)

a = np.array([[10, 0.1], [0.2, 3], [4, 0.6], [0.5, 0.6]])
print("a = np.array([[10, 0.1], [0.2, 3], [4, 0.6], [0.5, 0.6]])")
print(model.predict(a))
