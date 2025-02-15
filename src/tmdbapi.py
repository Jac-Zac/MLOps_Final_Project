import requests
import csv
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("\nmiao\n")

API_KEY = "miao"  # e.g. bau
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

all_movies = []

for page in range(1, 501):  # up to 500 pages
    params = {
        "api_key": API_KEY,
        # Sort by highest-rated first:
        "sort_by": "vote_average.desc",
        # Require at least a certain number of votes:
        "vote_count.gte": 1000,
        "page": page
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # If we actually get results, add them to our list
    if "results" in data:
        all_movies.extend(data["results"])
    else:
        # If something is off or we run out of results, break early
        break

print(f"Total movies fetched: {len(all_movies)}")
# Now all_movies holds up to 10,000 of the highest-rated films.


# Now we want to write only certain fields to CSV:
fields = [
    "genre_ids",
    "original_language",
    "original_title",
    "overview",
    "popularity",
    "poster_path",
    "vote_average",
    "title"
]

# Write results into a CSV file
with open("movies.csv", mode="w", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for movie in all_movies:
        # Make a filtered row with only the fields we want
        row = {field: movie.get(field, "") for field in fields}
        
        # If you want genre_ids to be a string rather than a list:
        # row["genre_ids"] = ",".join(str(genre) for genre in row["genre_ids"])
        
        writer.writerow(row)

print("CSV file 'movies.csv' has been created.")

df = pd.read_csv("movies.csv")

model = SentenceTransformer('all-MiniLM-L6-v2') #~llm
embeddings = model.encode(df['overview'].tolist(), convert_to_numpy=True)

embedding_dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dimension)  # L2 distance index
index.add(embeddings)  # Add embeddings to the index

faiss.write_index(index, "movies_faiss.index")

# faiss: facebook AI similarity search



