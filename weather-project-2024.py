# Importiamo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from geopy.distance import geodesic

# Step 1: Importare il dataset con Pandas
# Carichiamo il dataset delle temperature globali
data = pd.read_csv("./GlobalTemperatures.csv")

# Step 2: Esplorare i dati
# Visualizziamo le prime righe del dataset per avere un'idea del contenuto
print(data.head())

# Step 3: Pulizia del dataset

# Visualizzare il numero di valori mancanti per ciascuna colonna
print(data.isnull().sum())
# dt                                    0
# AverageTemperature               364130
# AverageTemperatureUncertainty    364130
# City                                  0
# Country                               0
# Latitude                              0
# Longitude                             0

# Rimuoviamo le righe con valori mancanti nelle colonne 'AverageTemperature' e 'AverageTemperatureUncertainty'
data_cleaned = data.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty'])

# Verifichiamo che i valori mancanti siano stati rimossi
print(data_cleaned.isnull().sum())
# dt                               0
# AverageTemperature               0
# AverageTemperatureUncertainty    0
# City                             0
# Country                          0
# Latitude                         0
# Longitude                        0