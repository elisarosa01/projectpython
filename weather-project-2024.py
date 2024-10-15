import pandas as pd
data = pd.read_csv("./GlobalTemperatures.csv")
print(data)

# Visualizza le prime righe del dataset
print(data.head())

# Mostra le informazioni sulle colonne e il tipo di dati
print(data.info())

# Statistiche descrittive generali sulle colonne numeriche
print(data.describe())

# Verifica se ci sono dati mancanti
print(data.isnull().sum())

# Rimuovi eventuali righe con dati mancanti, se appropriato
data_cleaned = data.dropna()
