from geopy.distance import geodesic

class RouteCalculator:
    def __init__(self, data, start_coords, end_coords):
        self.data = data
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.route = []

    def calculate_route(self):
        """Calculates the warmest route."""
        current_coords = self.start_coords
        route = [{'City': 'Start', 'Latitude': current_coords[0], 'Longitude': current_coords[1]}]
        data_copy = self.data.copy()

        while data_copy.shape[0] > 0:
            data_copy['Distance'] = data_copy.apply(
                lambda row: geodesic(current_coords, (row['Latitude'], row['Longitude'])).kilometers, axis=1)
            closest = data_copy.nsmallest(3, 'Distance')
            warmest = closest.loc[closest['AverageTemperature'].idxmax()]
            route.append({'City': warmest['City'], 'Latitude': warmest['Latitude'], 'Longitude': warmest['Longitude']})
            current_coords = (warmest['Latitude'], warmest['Longitude'])
            data_copy = data_copy[data_copy['City'] != warmest['City']]

        self.route = route
        return route
