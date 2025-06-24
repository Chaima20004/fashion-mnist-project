# Progetto Fashion-MNIST - Chaima Chourabi (VR510606)

![Distribuzione Classi](images/class_distribution.png)
![Training](images/training_history.png)


docker build -t fashion-mnist .
docker run -v $(pwd)/images:/app/images fashion-mnist

# Con Docker (Gradio):
docker run -p 8080:8080 -v $(pwd)/images:/app/images fashion-mnist
