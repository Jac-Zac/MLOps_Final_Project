import requests
import csv
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("movies_faiss.index")
df = pd.read_csv("movies.csv")


query = "psychological thriller"
query_embedding = model.encode([query], convert_to_numpy=True)
k = 5  # number of nearest neighbors
distances, indices = index.search(query_embedding, k)

print("Nearest neighbors (indices):", indices)
print("Distances:", distances)
print("Corresponding movies:", df.iloc[indices[0]])

for idx in indices[0]:  # Loop through the first (only) row of nearest neighbors
    print(f"Recommended Movie: {df.iloc[idx]['title']} ({df.iloc[idx]['vote_average']}/10)")


