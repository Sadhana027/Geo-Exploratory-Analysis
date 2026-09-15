# Geo Exploratory Analysis & Map Visualization

An interactive Streamlit application for exploring lifestyle and demographic survey data using data preprocessing, K-Means clustering, and Folium-based map visualization.

## Features

- Interactive selection of institutions
- User input for lifestyle preferences
- Data cleaning and feature selection using Pandas
- K-Means clustering to analyze patterns in the dataset
- Interactive map visualization using Folium
- Cluster-based visual analysis using Matplotlib and Seaborn
- Streamlit-based interactive dashboard

## Technologies Used

- Python
- Pandas
- Scikit-learn
- K-Means Clustering
- Streamlit
- Folium
- Streamlit-Folium
- Matplotlib
- Seaborn

## Project Workflow

1. Load the lifestyle and demographic survey dataset.
2. Select relevant features from the dataset for analysis.
3. Handle missing values using data preprocessing.
4. Accept lifestyle preference inputs through the Streamlit interface.
5. Add the selected preferences to the dataset for analysis.
6. Apply K-Means clustering to group similar records.
7. Visualize selected institution locations and preference-based markers using Folium.
8. Analyze cluster characteristics using box plots.

## Dataset

The project uses a coded lifestyle and food survey dataset containing variables related to:

- Food preferences
- Lifestyle habits
- Exercise
- Sports activity
- Eating-out frequency
- Income
- Other demographic and preference-related attributes

The dataset is included in this repository as `food_coded.csv`.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Sadhana027/Geo-Exploratory-Analysis.git
