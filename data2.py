import pandas as pd
import folium
from sklearn.cluster import KMeans
import numpy as np

# Function to clean data, perform clustering, and save it

def process_data(file_path):
    df = pd.read_csv(file_path)
    df = df[["cook", "diet_current_coded", "eating_out", "sports", "exercise", "fav_cuisine_coded", "on_off_campus", "pay_meal_out", "fav_food", "fruit_day", "income"]]
    df.dropna(axis=0, inplace=True)

    # Perform clustering
    k = 3
    kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
    df['Cluster'] = kmeans.labels_
    output_file = file_path.replace(".csv", "_with_clusters.csv")
    df.to_csv(output_file, index=False)
    return output_file

# Function to create a map for the selected city
def create_map(city):
    location_map = {
        "Hyderabad": [17.385044, 78.486671],
        "Delhi": [28.613939, 77.209023],
        "Bombay": [19.076090, 72.877426]
    }

    city_location = location_map.get(city)
    if city_location:
        city_map = folium.Map(location=city_location, zoom_start=12)
        city_map.save(f"map_{city.lower()}.html")
    else:
        raise ValueError("Invalid city name provided for map creation.")

# Function to get student preferences
def get_student_preferences():
    print("Enter your preferences:")
    cook = int(input("Cooking preference (1-5): "))
    diet = int(input("Diet preference coded (1-5): "))
    sports = int(input("Sports activity level (1-5): "))
    on_off_campus = int(input("Do you prefer on-campus or off-campus residents? (1 for On, 0 for Off): "))

    return {
        "cook": cook,
        "diet_current_coded": diet,
        "sports": sports,
        "on_off_campus": on_off_campus
    }

# Function to find nearby residents based on preferences
def find_nearby_residents(preferences, processed_file):
    df = pd.read_csv(processed_file)

    conditions = (
        (df['cook'] == preferences['cook']) &
        (df['diet_current_coded'] == preferences['diet_current_coded']) &
        (df['sports'] == preferences['sports']) &
        (df['on_off_campus'] == preferences['on_off_campus'])
    )

    results = df[conditions]
    return results
