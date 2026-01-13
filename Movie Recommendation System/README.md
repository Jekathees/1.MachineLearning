# Movie Recommendation System

## Overview
This project implements a **Content-Based Movie Recommendation System**.  
Users can input their favorite movie, and the system recommends similar movies based on **genres, keywords, cast, director, and tagline**.  

- Text features are combined into a single string for each movie.
- **TF-IDF vectorization** converts text data into numerical feature vectors.
- **Cosine similarity** is used to calculate similarity between movies.
- Users receive a list of the most similar movies based on their input.

---

## Dataset

### Dataset Source
The dataset used is a **movies dataset** containing metadata such as genres, cast, director, keywords, and tagline. 
---

## Methodology

### **1. Data Preprocessing**
- Fill missing values
- Combine relevant text features into one string for each movie:
  ```python
  combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
  ```

### **2. Feature Extraction**
- Convert combined text features into numerical vectors using **TF-IDF Vectorizer**
- Handles the importance of rare vs common words in movie descriptions

### **3. Compute Movie Similarity**
- Calculate **cosine similarity** between all movie vectors
- Similarity score indicates how closely movies are related

### **4. User Input & Recommendation**
- User inputs a favorite movie
- System finds the closest match to handle typos
- Retrieves similarity scores
- Sorts movies by similarity and recommends top 30 similar movies

---


## Features
- Handles typos in user input using `difflib.get_close_matches()`
- Recommends movies based on multiple metadata features
- Uses content-based similarity (no ratings required)
- Top 30 similar movies are recommended for any input

---

## How It Works

1. User enters a movie name.
2. System finds the closest match in the dataset.
3. TF-IDF feature vectors of all movies are computed.
4. Cosine similarity is calculated between the selected movie and all others.
5. Movies are sorted by similarity score.
6. Top N recommendations are displayed.

---

## Example Output

```
Enter your favourite movie name: Avengers

Movies suggested for you:

1. Avengers: Age of Ultron
2. Captain America: Civil War
3. Iron Man 3
...
...
