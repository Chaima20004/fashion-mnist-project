{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from tensorflow.keras.datasets import fashion_mnist\n",
    "\n",
    "# Carica i dati\n",
    "(X_train, y_train), _ = fashion_mnist.load_data()\n",
    "classes = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', \n",
    "           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']\n",
    "\n",
    "# 1. Distribuzione delle classi\n",
    "plt.figure(figsize=(10,5))\n",
    "plt.hist(y_train, bins=10, rwidth=0.8)\n",
    "plt.xticks(range(10), classes, rotation=45)\n",
    "plt.savefig('images/class_distribution.png')\n",
    "\n",
    "# 2. Esempi di immagini\n",
    "plt.figure(figsize=(10,10))\n",
    "for i in range(25):\n",
    "    plt.subplot(5,5,i+1)\n",
    "    plt.imshow(X_train[i], cmap='gray')\n",
    "    plt.title(classes[y_train[i]])\n",
    "    plt.axis('off')\n",
    "plt.savefig('images/sample_images.png')"
   ]
  }
 ]
}