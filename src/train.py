import os
os.makedirs('../images', exist_ok=True)

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Caricamento dati
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

# Modello
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestramento
history = model.fit(X_train, y_train, epochs=3, validation_data=(X_test, y_test))

# Grafico
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Andamento Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoca')
plt.legend(['Train', 'Validation'])
plt.savefig('../images/training_history.png')
print('Grafico salvato in ../images/training_history.png')
