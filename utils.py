import requests

API_KEY = ""  # Replace with your actual TMDB API key

def fetch_poster(movie_id):
    """
    Given a TMDB movie ID, return the full URL of the poster image.
    If no poster found, returns a placeholder URL.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/150"
    except:
        return "https://via.placeholder.com/150"
