import pandas as pd

# Importing the dataset
df_movies = pd.read_csv('Main/ml-25m/movies.csv', usecols=["movieId", "title"])
df_ratings = pd.read_csv('Main/ml-25m/ratings.csv', usecols=["movieId", "rating"])

# Merge the two dataframes on 'movieId' column
merged_df = pd.merge(df_movies, df_ratings, on='movieId')

# Calculate average ratings and number of ratings for each movie
avg_rating = pd.DataFrame(merged_df.groupby('title')['rating'].mean())
avg_rating['num_ratings'] = pd.DataFrame(merged_df.groupby('title')['rating'].count())

# Define weights for the parameters (you can adjust these values)
weight_avg_rating = 250
weight_num_ratings = 0.01

# Calculate a combined score
avg_rating['combined_score'] = (avg_rating['rating'] * weight_avg_rating) + (avg_rating['num_ratings'] * weight_num_ratings)

# Sort by the combined score in descending order
top_movies = avg_rating.sort_values(by='combined_score', ascending=False).head(10)

# Create new file with users favorite movies
top_movies.to_csv('Main/top_movies.csv')

# Print the top 10 movies based on the combined score
print("Top 10 best movies:")
print(top_movies)

