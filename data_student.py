import data2
from tabulate import tabulate

# Step 1: Allow the user to select a city
print("Select a city:")
print("1. Hyderabad")
print("2. Delhi")
print("3. Bombay")

city_choice = int(input("Enter the number corresponding to your choice: "))
city_map = {
    1: "Hyderabad",
    2: "Delhi",
    3: "Bombay"
}

selected_city = city_map.get(city_choice, None)
if not selected_city:
    print("Invalid choice. Please restart the program and select a valid city.")
    exit()

print(f"You selected: {selected_city}")

# Generate and save the map for the selected city
data2.create_map(selected_city)
print(f"Map for {selected_city} has been saved as 'map_{selected_city.lower()}.html'.")

# Step 2: Collect user preferences
preferences = data2.get_student_preferences()

# Step 3: Process data and find nearby residents
data_file = r"C:\Users\Keerthi Sowmya\OneDrive\Documents\MAGGIE\Geo Exploratory Analysis\food_choices_with_clusters.csv"
results = data2.find_nearby_residents(preferences, data_file)

# Step 4: Display results
if results.empty:
    print("No matching residents found based on your preferences.")
else:
    print("Here are the nearby residents that match your preferences:")
    print(tabulate(results, headers='keys', tablefmt='psql'))
