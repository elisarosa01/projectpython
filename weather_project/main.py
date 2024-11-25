from data_cleaning import load_and_clean_data
from analysis import analyze_temperature_changes, plot_std_temp_variability
from visualization import plot_top_cities_temperature, plot_city_temperature_change
from route_calculation import calculate_and_plot_route

def main():
    # Load and clean data
    city_data = load_and_clean_data("data/GlobalLandTemperaturesByCity.csv")
    major_city_data = load_and_clean_data("data/GlobalLandTemperaturesByMajorCity.csv")

    # Analysis
    analyze_temperature_changes(city_data)

    # Visualization
    plot_std_temp_variability(city_data)

    # Route Calculation
    calculate_and_plot_route(major_city_data)

if __name__ == "__main__":
    main()
