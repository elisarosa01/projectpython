from data_preprocessing import DataPreprocessor
from analysis_visualization import DataAnalyzer
from route_calculation import RouteCalculator
from utilities import Utils

# Step 1: Load and clean data
preprocessor = DataPreprocessor("data/GlobalLandTemperaturesByCity.csv")
raw_data = preprocessor.load_data()
cleaned_data = preprocessor.clean_data()

# Step 2: Perform analysis
analyzer = DataAnalyzer(cleaned_data)
periods = {"1743-1796": (1743, 1796), "1797-1850": (1797, 1850)}
results = analyzer.analyze_temperature_changes(periods)
analyzer.plot_temperature_changes(periods, results)

# Step 3: Calculate warmest route
start = (39.9042, 116.4074)  # Beijing
end = (34.0522, -118.2437)  # Los Angeles
calculator = RouteCalculator(cleaned_data, start, end)
route = calculator.calculate_route()
print("Warmest Route:", route)
