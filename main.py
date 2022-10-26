import numpy as np
import tensorflow as tf
from PIL import Image
from os import listdir
import numpy as np
from sklearn.model_selection import train_test_split


a = 12345
isk = 'insoo'

label = np.load('D:\Workspace\SW_academy/label.npy')
label = tf.keras.utils.to_categorical(label.astype('int8') - 1)
data = np.load('D:\Workspace\SW_academy/data.npy')

X_train, X_test, y_train, y_test = train_test_split(data, label, stratify=label)

X_train = tf.convert_to_tensor(X_train)
X_test = tf.convert_to_tensor(X_test)
y_train = tf.convert_to_tensor(y_train)
y_test = tf.convert_to_tensor(y_test)


class MyModel(tf.keras.models.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(10, (9, 9), activation=tf.keras.activations.relu)
        self.pool1 = tf.keras.layers.MaxPool2D(pool_size=(4, 4))
        self.conv2 = tf.keras.layers.Conv2D(5, (6, 6), activation=tf.keras.activations.relu)
        self.pool2 = tf.keras.layers.MaxPool2D(pool_size=(3, 3))
        self.conv3 = tf.keras.layers.Conv2D(2, (4, 4), activation=tf.keras.activations.relu)
        self.flatten = tf.keras.layers.Flatten()
        self.dense1 = tf.keras.layers.Dense(100, activation='relu')
        self.dense2 = tf.keras.layers.Dense(4, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x

model = MyModel()

loss_object = tf.keras.losses.CategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.CategoricalAccuracy(name='train_accuracy')

test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.CategoricalAccuracy(name='test_accuracy')

@tf.function
def train_step(images, labels):
    with tf.GradientTape() as tape:
        # training=True is only needed if there are layers with different
        # behavior during training versus inference (e.g. Dropout).
        predictions = model(images, training=True)
        loss = loss_object(labels, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    train_loss(loss)
    train_accuracy(labels, predictions)

@tf.function
def test_step(images, labels):
    # training=False is only needed if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    predictions = model(images, training=False)
    t_loss = loss_object(labels, predictions)

    test_loss(t_loss)
    test_accuracy(labels, predictions)

EPOCHS = 20

for epoch in range(EPOCHS):
    # Reset the metrics at the start of the next epoch
    train_loss.reset_states()
    train_accuracy.reset_states()
    test_loss.reset_states()
    test_accuracy.reset_states()

    for batch in range(58):
        if batch == 57:
            train_step(X_train[batch * 32:, :, :, :], y_train[batch * 32:])
        else:
            train_step(X_train[batch * 32:(batch + 1) * 32, :, :, :], y_train[batch * 32:(batch + 1) * 32])

    for batch in range(20):
        if batch == 19:
            test_step(X_train[batch * 32:, :, :, :], y_train[batch * 32:])
        else:
            test_step(X_test[batch * 32:(batch + 1) * 32, :, :, :], y_train[batch * 32:(batch + 1) * 32])

    print(
        f'Epoch {epoch + 1}, '
        f'Loss: {train_loss.result()}, '
        f'Accuracy: {train_accuracy.result() * 100}, '
        f'Test Loss: {test_loss.result()}, '
        f'Test Accuracy: {test_accuracy.result() * 100}'
    )
