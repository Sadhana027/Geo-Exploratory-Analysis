import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data cleaning and extracting relevant features
df1 = pd.read_csv(r"C:\Users\Keerthi Sowmya\OneDrive\Documents\MAGGIE\Geo Exploratory Analysis\food_coded.csv")
df = df1[["cook", "diet_current_coded", "eating_out", "sports", "exercise", "fav_cuisine_coded", "on_off_campus", "pay_meal_out", "fav_food", "fruit_day", "income"]]

# Dropping rows with NaN values
df = df.dropna(axis=0)

# Option to add an extra row dynamically
new_row = {
    "cook": 2,  # Replace with the actual values you want to input
    "diet_current_coded": 1,
    "eating_out": 3,
    "sports": 2,
    "exercise": 1,
    "fav_cuisine_coded": 2,
    "on_off_campus": 1,
    "pay_meal_out": 2,
    "fav_food": 3,
    "fruit_day": 4,
    "income": 5
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

plt.show()
