import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape
import os

# Crea la cartella images se non esiste
os.makedirs('images', exist_ok=True)

# Caricamento dati
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0  # Normalizza

# Modello semplice
model = Sequential([
    Reshape((28*28,), input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestramento
history = model.fit(X_train, y_train, 
                    epochs=5, 
                    validation_data=(X_test, y_test),
                    verbose=1)

# Grafico di training
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Accuracy (training)')
plt.plot(history.history['val_accuracy'], label='Accuracy (validation)')
plt.title('Andamento Accuracy durante il Training')
plt.xlabel('Epoca')
plt.ylabel('Accuracy')
plt.legend()

# Salva l'immagine
plt.savefig('images/training_history.png', bbox_inches='tight', dpi=100)
print('Immagine salvata in: images/training_history.png')
