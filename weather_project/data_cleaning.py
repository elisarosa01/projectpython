import pandas as pd

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)

    # Remove missing values
    data = data.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty'])

    # Convert 'dt' to datetime
    data['dt'] = pd.to_datetime(data['dt'], errors='coerce')

    # Convert latitude and longitude to numeric values
    data['Latitude'] = data['Latitude'].apply(
        lambda x: float(x[:-1]) * (-1 if 'S' in x or 'W' in x else 1)
    )
    data['Longitude'] = data['Longitude'].apply(
        lambda x: float(x[:-1]) * (-1 if 'S' in x or 'W' in x else 1)
    )

    # Extract the year
    data['Year'] = data['dt'].dt.year

    return data

