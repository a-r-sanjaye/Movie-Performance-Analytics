

# 📦 Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from collections import Counter

# 🧩 Step 1: Load Dataset
print("🔹 Loading dataset...")
df = pd.read_csv("tmdb_5000_movies.csv")

print("✅ Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

# 🧹 Step 2: Data Cleaning
print("\n🔹 Cleaning data...")

# Select important columns
df = df[['title', 'budget', 'revenue', 'runtime', 'vote_average',
         'vote_count', 'genres', 'release_date']]

# Drop missing values
df.dropna(inplace=True)

# Convert release_date to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Extract year
df['year'] = df['release_date'].dt.year

# Convert budget and revenue to numeric
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

print("✅ Cleaning completed!")
print("\nDataset Info:")
print(df.info())

# 🧠 Step 3: Basic Statistics
print("\n🔹 Basic Statistics:")
print(df.describe())



sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# 1️⃣ Budget vs Ratings
print("\n📈 Plotting Budget vs Ratings...")
sns.scatterplot(x='budget', y='vote_average', data=df)
plt.title("Budget vs Ratings")
plt.xlabel("Budget (in $)")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# 2️⃣ Revenue vs Ratings
print("\n📈 Plotting Revenue vs Ratings...")
sns.scatterplot(x='vote_average', y='revenue', data=df)
plt.title("Ratings vs Revenue")
plt.xlabel("Average Rating")
plt.ylabel("Revenue (in $)")
plt.tight_layout()
plt.show()

# 3️⃣ Top 10 Highest Rated Movies
print("\n🏆 Top 10 Highest Rated Movies:")
top_rated = df.sort_values(by='vote_average', ascending=False).head(10)
print(top_rated[['title', 'vote_average']])

plt.figure(figsize=(10, 5))
sns.barplot(x='vote_average', y='title', data=top_rated, palette='mako')
plt.title("Top 10 Highest Rated Movies")
plt.xlabel("Rating")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

# 4️⃣ Top 10 Revenue-Generating Movies
print("\n💰 Top 10 Revenue-Generating Movies:")
top_revenue = df.sort_values(by='revenue', ascending=False).head(10)
print(top_revenue[['title', 'revenue']])

plt.figure(figsize=(10, 5))
sns.barplot(x='revenue', y='title', data=top_revenue, palette='viridis')
plt.title("Top 10 Revenue-Generating Movies")
plt.xlabel("Revenue (in $)")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

# 5️⃣ Popular Genres Analysis
print("\n🎭 Analyzing genres...")

# Parse genres column (JSON-like string)
df['genres'] = df['genres'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)] if pd.notna(x) else [])
genre_list = df['genres'].sum()
genre_count = Counter(genre_list)

# Convert to DataFrame for plotting
genre_df = pd.DataFrame(genre_count.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Genre', y='Count', data=genre_df, palette='coolwarm')
plt.title("Most Frequent Movie Genres")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6️⃣ Trend of Movies Over Years
print("\n📆 Analyzing movie release trends...")
yearly_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o')
plt.title("Number of Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()



df.to_csv("cleaned_tmdb_data.csv", index=False)
print("\n💾 Cleaned dataset saved as 'cleaned_tmdb_data.csv'")


print("\n✅ PROJECT SUMMARY")
print("-----------------------")
print(f"Total Movies Analyzed: {len(df)}")
print(f"Average Rating: {df['vote_average'].mean():.2f}")
print(f"Average Budget: ${df['budget'].mean():.2f}")
print(f"Average Revenue: ${df['revenue'].mean():.2f}")
print("\n🎉 Analysis Completed Successfully!")
