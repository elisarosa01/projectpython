import pandas as pd

class DataPreprocessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.cleaned_data = None

    def load_data(self):
        """Loads the dataset from the given file path."""
        self.data = pd.read_csv(self.filepath)
        return self.data

    def clean_data(self):
        """Cleans the dataset by handling missing values and formatting."""
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        data = self.data.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty']).copy()
        data['dt'] = pd.to_datetime(data['dt'], errors='coerce')
        data['Latitude'] = data['Latitude'].apply(
            lambda x: float(x[:-1]) * (-1 if 'S' in x or 'W' in x else 1)
        )
        data['Longitude'] = data['Longitude'].apply(
            lambda x: float(x[:-1]) * (-1 if 'S' in x or 'W' in x else 1)
        )
        data['Year'] = data['dt'].dt.year
        self.cleaned_data = data
        return self.cleaned_data

