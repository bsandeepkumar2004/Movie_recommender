import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Global cache for similarity matrix
_similarity_matrix = None
_titles = None
_movies_with_features = None

def load_data():
    movies = pd.read_csv("data/tmdb_5000_movies.csv")

    # Combine features like genres, keywords, and tagline
    def process_row(row):
        genres = ast.literal_eval(row['genres']) if pd.notna(row['genres']) else []
        genre_names = ' '.join([genre['name'] for genre in genres])
        
        keywords = ast.literal_eval(row['keywords']) if pd.notna(row['keywords']) else []
        keyword_names = ' '.join([kw['name'] for kw in keywords])

        tagline = row['tagline'] if pd.notna(row['tagline']) else ''

        return f"{row['title']} {genre_names} {keyword_names} {tagline}"

    movies['combined_features'] = movies.apply(process_row, axis=1)

    # Store for global use
    global _movies_with_features, _titles
    _movies_with_features = movies
    _titles = movies['title'].tolist()

    return movies


def build_similarity_matrix():
    global _similarity_matrix
    if _similarity_matrix is None:
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(_movies_with_features['combined_features'])
        _similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)


def recommend_by_title(movies, movie_name):
    build_similarity_matrix()
    movie_name = movie_name.lower()

    try:
        idx = next(i for i, title in enumerate(_titles) if movie_name in title.lower())
    except StopIteration:
        return pd.DataFrame(columns=['title', 'vote_average', 'popularity', 'overview'])

    sim_scores = list(enumerate(_similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]
    return _movies_with_features.iloc[movie_indices][['title', 'vote_average', 'popularity', 'overview']]


def recommend_by_genre(movies, genre_name):
    def genre_match(genre_str):
        try:
            genres = ast.literal_eval(genre_str)
            return any(genre['name'].lower() == genre_name.lower() for genre in genres)
        except:
            return False

    filtered = movies[movies['genres'].apply(genre_match)]
    filtered = filtered.sort_values(by='popularity', ascending=False)
    return filtered[['title', 'vote_average', 'popularity', 'overview']]


def get_top_rated(movies, min_rating=4.0):
    filtered = movies[movies['vote_average'] >= min_rating]
    filtered = filtered.sort_values(by='vote_average', ascending=False)
    return filtered[['title', 'vote_average', 'popularity', 'overview']]


def get_most_popular(movies):
    filtered = movies.sort_values(by='popularity', ascending=False)
    return filtered[['title', 'vote_average', 'popularity', 'overview']]


# recommender.py

