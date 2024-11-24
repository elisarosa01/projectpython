class Utils:
    @staticmethod
    def calculate_std(data):
        """Calculates temperature standard deviation."""
        return data.groupby(['City', 'Country'])['AverageTemperature'].std().reset_index()
