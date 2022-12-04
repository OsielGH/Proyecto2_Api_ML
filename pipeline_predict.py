import joblib
import config1 as cfg
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
Titanic_model = joblib.load('Survived_pipeline.pkl')

#Funcion para hacer predicciones.
def predict(X):
    predicts = Titanic_model.predict(X)
    salida = np.exp(predicts)
    print(salida)
    return salida[0]


    