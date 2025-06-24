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
    "import os\n",
    "\n",
    "# Crea la cartella images se non esiste\n",
    "os.makedirs('images', exist_ok=True)\n",
    "\n",
    "# Carica i dati\n",
    "(_, y_train), _ = fashion_mnist.load_data()\n",
    "classes = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', \n",
    "           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']\n",
    "\n",
    "# Grafico a barre\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.hist(y_train, bins=10, rwidth=0.8, color='skyblue')\n",
    "plt.xticks(range(10), classes, rotation=45)\n",
    "plt.title('Distribuzione delle Classi Fashion-MNIST')\n",
    "plt.xlabel('Classi')\n",
    "plt.ylabel('Conteggio')\n",
    "\n",
    "# Salva l'immagine\n",
    "plt.savefig('images/class_distribution.png', bbox_inches='tight', dpi=100)\n",
    "print('Immagine salvata in: images/class_distribution.png')"
   ]
  }
 ]
}
