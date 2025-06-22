import gradio as gr
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("model.h5")
labels = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
          'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def predict(img):
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255
    pred = model.predict(img)[0]
    return {labels[i]: float(pred[i]) for i in range(10)}

gr.Interface(
    fn=predict,
    inputs=gr.Sketchpad(shape=(28,28), image_mode='L'),
    outputs=gr.Label(num_top_classes=3),
    title="Classificatore Fashion-MNIST"
).launch(server_port=8080)