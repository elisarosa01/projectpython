import matplotlib.pyplot as plt
import numpy as np

class DataAnalyzer:
    def __init__(self, cleaned_data):
        self.data = cleaned_data

    def analyze_temperature_changes(self, periods):
        """Analyzes temperature changes over defined periods."""
        annual_avg_temp = self.data.groupby(['City', 'Country', 'Year'])['AverageTemperature'].mean().reset_index()
        period_results = {}
        for period_name, (start_year, end_year) in periods.items():
            period_data = annual_avg_temp[(annual_avg_temp['Year'] >= start_year) & (annual_avg_temp['Year'] <= end_year)]
            temp_start = period_data[period_data['Year'] == start_year].set_index(['City', 'Country'])['AverageTemperature']
            temp_end = period_data[period_data['Year'] == end_year].set_index(['City', 'Country'])['AverageTemperature']
            temp_change = pd.merge(temp_start, temp_end, left_index=True, right_index=True, suffixes=('_start', '_end'))
            temp_change['TemperatureChange'] = temp_change['AverageTemperature_end'] - temp_change['AverageTemperature_start']
            temp_change.reset_index(inplace=True)
            period_results[period_name] = temp_change.nlargest(3, 'TemperatureChange')
        return period_results

    def plot_temperature_changes(self, periods, period_results):
        """Plots temperature changes for the given periods."""
        plt.figure(figsize=(14, 8))
        period_colors = ['#f0f8ff', '#e6e6fa', '#fff0f5', '#f5f5dc', '#e0ffff']
        colors = ['red', 'green', 'blue']
        markers = ['o', 's', '^']

        for i, (period_name, (start_year, end_year)) in enumerate(periods.items()):
            plt.axvspan(start_year, end_year, color=period_colors[i], alpha=0.3, label=f"Period {period_name}")
            top_cities = period_results[period_name]
            for rank, (_, row) in enumerate(top_cities.iterrows()):
                city = row['City']
                country = row['Country']
                city_data = self.data[(self.data['City'] == city) & (self.data['Country'] == country) & 
                                      (self.data['Year'] >= start_year) & (self.data['Year'] <= end_year)]
                plt.plot(city_data['Year'], city_data['AverageTemperature'], label=f"{rank + 1}. {city} ({country})",
                         color=colors[rank], marker=markers[rank])

        plt.legend(title="Top Cities by Period", loc='upper left')
        plt.title("Temperature Changes Across Historical Periods")
        plt.xlabel("Year")
        plt.ylabel("Average Temperature (°C)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
