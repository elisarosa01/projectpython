import pandas as pd
import matplotlib.pyplot as plt

def analyze_temperature_changes(data):
    # Your analysis logic for top cities by temperature changes
    print("Analyzing temperature changes...")
    # Placeholder: Perform calculations and analysis as needed

def calculate_temp_std(data):
    temp_std = data.groupby(['City', 'Country'])['AverageTemperature'].std().reset_index()
    temp_std.columns = ['City', 'Country', 'TemperatureStd']
    return temp_std

def plot_std_temp_variability(data):
    temp_std = calculate_temp_std(data)
    top_cities = temp_std.nlargest(10, 'TemperatureStd')

    # Plot standard deviation
    plt.figure(figsize=(12, 6))
    plt.bar(top_cities['City'], top_cities['TemperatureStd'], color='orange')
    plt.title('Top 10 Cities by Temperature Variability (Standard Deviation)')
    plt.xlabel('City')
    plt.ylabel('Temperature Std (°C)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
