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

# Convertire la colonna 'dt' in formato datetime 
data_cleaned['dt'] = pd.to_datetime(data_cleaned['dt'])

# Verifica il tipo di dato della colonna 'dt'
print(data_cleaned.dtypes)

# Per adesso selezioniamo alcune città e vediamo com'è cambiata la 
# temperatura negli anni

# Step 4: Filtriamo i dati dal 1750
data_filtered = data_cleaned[data_cleaned['dt'] >= '1750-01-01']

# Step 5: Aggregazione delle temperature medie per paese e anno
# Estraiamo l'anno dalla colonna 'dt'
data_filtered['Year'] = data_filtered['dt'].dt.year

# Calcoliamo la temperatura media per ogni anno e paese
avg_temp_by_country = data_filtered.groupby(['Country', 'Year'])['AverageTemperature'].mean().reset_index()

# Step 6: Selezioniamo alcuni paesi per la visualizzazione
countries_of_interest = ['United Kingdom', 'Germany', 'United States', 'China', 'India']
filtered_data = avg_temp_by_country[avg_temp_by_country['Country'].isin(countries_of_interest)]

# Step 7: Creiamo un grafico
plt.figure(figsize=(14, 8))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['AverageTemperature'], label=country)

# Aggiungiamo titoli e etichette
plt.title('Cambiamento della Temperatura Media per Paese (1750 - Oggi)')
plt.xlabel('Anno')
plt.ylabel('Temperatura Media (°C)')
plt.grid(True)
plt.legend()

# Mostriamo il grafico
plt.show()