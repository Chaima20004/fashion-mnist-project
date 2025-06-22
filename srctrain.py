from tensorflow.keras.datasets import fashion_mnist
from model import build_model
import matplotlib.pyplot as plt

def main():
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    model = build_model()
    history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
    
    model.save("model.h5")
    
    # Salva il grafico di training
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('images/training_history.png')

if __name__ == "__main__":
    main()