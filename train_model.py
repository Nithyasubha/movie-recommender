import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load data
df = pd.read_csv("movies.csv")

# Convert genre to vectors
cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

# Compute similarity
similarity = cosine_similarity(matrix)

# Save model
pickle.dump((df, similarity), open("model.pkl", "wb"))

print("Model saved successfully!")