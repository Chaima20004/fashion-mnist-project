# Progetto Fashion-MNIST - Chaima Chourabi (VR510606)

![Distribuzione Classi](images/class_distribution.png)
![Training](images/training_history.png)

## Come eseguire
```bash
# Con Docker (addestramento):
docker build -t fashion-mnist .
docker run -v $(pwd)/images:/app/images fashion-mnist

# Con Docker (Gradio):
docker run -p 8080:8080 -v $(pwd)/images:/app/images fashion-mnist

## Note
- Le immagini (`class_distribution.png` e `training_history.png`) non sono incluse per problemi tecnici,  
  ma il codice per generarle è presente in `notebooks/eda.ipynb` e `src/train.py`.
