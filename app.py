import streamlit as st
import folium
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from streamlit_folium import st_folium

# Title for the app
st.title("Geo Exploratory Analysis and Map Visualization")

# Sidebar for user inputs
st.sidebar.header("User Preferences")
location_selector = st.sidebar.selectbox("Select an Institution:", 
    ["IIT Bombay", "NITIE Mumbai", "IIT Hyderabad", "NIT Warangal", "IIT Delhi", "NIT Delhi"])

sports = st.sidebar.slider("Sports Activity (1-5):", 1, 5, 3)
eating_out = st.sidebar.slider("Eating Out (1-5):", 1, 5, 3)
income = st.sidebar.slider("Income Level (1-5):", 1, 5, 3)

# Display user preferences
st.write(f"Preferences for {location_selector}:")
st.write(f"Sports Activity: {sports}, Eating Out: {eating_out}, Income Level: {income}")

# Institution data with coordinates for map visualization
institution_data = {
    "IIT Bombay": {"location": [19.1334, 72.9133], "name": "IIT Bombay"},
    "NITIE Mumbai": {"location": [19.1120, 72.9081], "name": "NITIE Mumbai"},
    "IIT Hyderabad": {"location": [17.4457, 78.3498], "name": "IIT Hyderabad"},
    "NIT Warangal": {"location": [17.4933, 78.3910], "name": "NIT Warangal"},
    "IIT Delhi": {"location": [28.5450, 77.1926], "name": "IIT Delhi"},
    "NIT Delhi": {"location": [28.7498, 77.1173], "name": "NIT Delhi"}
}

# Add custom map marker for selected institution
selected_institution = institution_data[location_selector]
institution_location = selected_institution["location"]

# Create the map
osm_map = folium.Map(location=institution_location, zoom_start=12)

# Add a marker for the selected institution
folium.Marker(institution_location, popup=selected_institution["name"]).add_to(osm_map)
# Add a marker for the selected institution with a red location icon
folium.Marker(
    institution_location, 
    popup=selected_institution["name"], 
    icon=folium.Icon(color='red', icon='info-sign', icon_color='white', prefix='fa')
).add_to(osm_map)

# Add a marker for the user preferences
user_marker_location = [institution_location[0] + (sports * 0.01), institution_location[1] + (income * 0.01)]
user_marker_popup = f"User Preferences: Sports Activity = {sports}, Eating Out = {eating_out}, Income Level = {income}"

folium.Marker(
    user_marker_location, 
    popup=user_marker_popup, 
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(osm_map)

# Display the map
st_folium(osm_map, width=700, height=500)

# Data cleaning and extracting relevant features
try:
    df1 = pd.read_csv(r"C:\Users\Keerthi Sowmya\OneDrive\Documents\MAGGIE\Geo Exploratory Analysis\food_coded.csv")
except FileNotFoundError:
    st.error("The file 'food_coded.csv' was not found. Please ensure the path is correct.")
    st.stop()

# Select relevant columns
df = df1[["cook", "diet_current_coded", "eating_out", "sports", "exercise", "fav_cuisine_coded", "on_off_campus", "pay_meal_out", "fav_food", "fruit_day", "income"]]

# Dropping rows with NaN values
df = df.dropna(axis=0)

# Option to add an extra row dynamically
new_row = {
    "cook": 2,  # Replace with the actual values you want to input
    "diet_current_coded": 1,
    "eating_out": eating_out,
    "sports": sports,
    "exercise": 1,
    "fav_cuisine_coded": 2,
    "on_off_campus": 1,
    "pay_meal_out": 2,
    "fav_food": 3,
    "fruit_day": 4,
    "income": income
}

# Convert the new row into a DataFrame and concatenate it to the original DataFrame
new_row_df = pd.DataFrame([new_row])  # Wrapping the new row in a DataFrame
df = pd.concat([df, new_row_df], ignore_index=True)  # Concatenate the new row

# K-Means clustering on cleaned data
k = 3
kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
df['Cluster'] = kmeans.labels_

# Plotting boxplots for each cluster
fig, axes = plt.subplots(1, k, sharey=True, figsize=(15, 5))
axes[0].set_ylabel('Coded Values', fontsize=12)

for i in range(k):
    plt.sca(axes[i])
    sns.boxplot(data=df[df['Cluster'] == i].drop('Cluster', axis=1), palette="Set1", ax=axes[i])
    axes[i].set_title(f'Cluster {i}', fontsize=12)
    # Rotate x-axis labels to avoid overlap
    plt.xticks(rotation=45, ha='right')

# Display the plots
st.pyplot(fig)
