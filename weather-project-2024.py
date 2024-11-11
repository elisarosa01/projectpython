# Importiamo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from geopy.distance import geodesic
import numpy as np

# Step 1: Importare il dataset con Pandas
# Carichiamo il dataset delle temperature globali
data = pd.read_csv("./GlobalTemperatures.csv")

# Step 2: Esplorare i dati
# Step 2.1. Visualizziamo le prime righe del dataset per avere un'idea del contenuto
print(data.head())
#           dt  AverageTemperature  AverageTemperatureUncertainty   City  \
# 0  1743-11-01               6.068                          1.737  Århus   
# 1  1743-12-01                 NaN                            NaN  Århus   
# 2  1744-01-01                 NaN                            NaN  Århus   
# 3  1744-02-01                 NaN                            NaN  Århus   
# 4  1744-03-01                 NaN                            NaN  Århus   

#    Country Latitude Longitude  
# 0  Denmark   57.05N    10.33E  
# 1  Denmark   57.05N    10.33E  
# 2  Denmark   57.05N    10.33E  
# 3  Denmark   57.05N    10.33E  
# 4  Denmark   57.05N    10.33E  

# Step 2.2. Per vedere tutte le città presenti nel dataset:
# creare un DataFrame con città uniche
unique_cities = data_cleaned[['City', 'Country']].drop_duplicates().reset_index(drop=True)

# Stampiamo l'elenco delle città
print("Numero totale di città uniche nel dataset:", len(unique_cities))
print(unique_cities)
# Numero totale di città uniche nel dataset: 3490

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

# Crea una copia esplicita del DataFrame pulito
data_cleaned = data.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty']).copy()

# Ora converti la colonna 'dt' in formato datetime senza warnings
data_cleaned['dt'] = pd.to_datetime(data_cleaned['dt'], errors='coerce')

# Verifica se ci sono valori nulli dopo la conversione
print(data_cleaned['dt'].isnull().sum())

# Verifica il tipo di dato della colonna 'dt'
print(data_cleaned.dtypes)

# dt                               datetime64[ns]
# AverageTemperature                      float64
# AverageTemperatureUncertainty           float64
# City                                     object
# Country                                  object
# Latitude                                 object
# Longitude                                object

# Conversione di Latitude e Longitude da object a float
# Funzione per convertire latitudine/longitudine in float
def convert_lat_lon(value):
    if 'N' in value or 'E' in value:
        return float(value[:-1])
    elif 'S' in value or 'W' in value:
        return -float(value[:-1])
    return float(value)

# Applica la funzione alle colonne Latitude e Longitude
data_cleaned['Latitude'] = data_cleaned['Latitude'].apply(convert_lat_lon)
data_cleaned['Longitude'] = data_cleaned['Longitude'].apply(convert_lat_lon)

# Controlliamo che ora i tipi siano corretti
print(data_cleaned.dtypes)

# dt                               datetime64[ns]
# AverageTemperature                      float64
# AverageTemperatureUncertainty           float64
# City                                     object
# Country                                  object
# Latitude                                float64
# Longitude                               float64

# Estraiamo l'anno dalla colonna 'dt'
data_cleaned['Year'] = data_cleaned['dt'].dt.year

# Trova l'ultimo anno presente nel dataset
last_year = data_cleaned['Year'].max()
print(f"L'ultimo anno presente nel dataset è: {last_year}")
# L'ultimo anno presente nel dataset è: 2013