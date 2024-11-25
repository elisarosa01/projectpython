import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def calculate_and_plot_route(data):
    start_city = {'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074}
    end_city = {'City': 'Los Angeles', 'Latitude': 34.0522, 'Longitude': -118.2437}

    year = int(input("Select a year between 1743 and 2013: "))
    filtered_data = data[data['Year'] == year]

    route = calculate_warmest_route(
        filtered_data,
        start_coords=(start_city['Latitude'], start_city['Longitude']),
        end_coords=(end_city['Latitude'], end_city['Longitude'])
    )
    plot_route(route, year)

def calculate_warmest_route(data, start_coords, end_coords):
    # Logic for calculating the warmest route
    return []  # Replace with actual route calculation

def plot_route(route, year):
    lons = [step['Longitude'] for step in route]
    lats = [step['Latitude'] for step in route]
    cities = [step['City'] for step in route]

    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.add_feature(cfeature.LAND, facecolor='lightgrey')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.BORDERS, linestyle='--')
    ax.add_feature(cfeature.COASTLINE)

    # Plot route
    for i in range(len(lons) - 1):
        ax.plot([lons[i], lons[i + 1]], [lats[i], lats[i + 1]], 'b--', transform=ccrs.Geodetic())
    for lon, lat, city in zip(lons, lats, cities):
        ax.plot(lon, lat, 'ro', transform=ccrs.PlateCarree())
        ax.text(lon + 2, lat - 1, city, transform=ccrs.PlateCarree())

    ax.set_title(f"Route from Beijing to Los Angeles (Year {year})")
    ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
    plt.show()
