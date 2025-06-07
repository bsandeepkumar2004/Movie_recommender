
import streamlit as st
from recommender import (
    load_data,
    recommend_by_title,
    recommend_by_genre,
    get_top_rated,
    get_most_popular,
)

st.set_page_config(page_title="Movie Recommendation App", layout="wide")

st.sidebar.title("🎬 Navigation")
mode = st.sidebar.radio("Select Recommendation Type", [
    "Home",
    "By Movie Title",
    "By Genre",
    "Top Rated Movies",
    "Most Popular Movies"
])

st.title("🍿 Movie Recommendation System")

movies = load_data()

PAGE_SIZE = 10

def show_movie_cards(movie_df):
    for _, row in movie_df.iterrows():
        st.markdown(f"### 🎬 {row['title']}")
        st.markdown(f"**⭐ Rating:** {row['vote_average']} &nbsp;&nbsp; 📊 Popularity: {row['popularity']:.1f}")
        st.markdown(f"📝 {row['overview']}")
        st.markdown("---")

# Initialize pagination counters in session state
if 'genre_page' not in st.session_state:
    st.session_state.genre_page = 0
if 'top_rated_page' not in st.session_state:
    st.session_state.top_rated_page = 0
if 'popular_page' not in st.session_state:
    st.session_state.popular_page = 0

if mode == "Home":
    # Clear session state variables related to recommendations
    keys_to_clear = [
        'genre_shown', 'genre_page', 'prev_genre',
        'top_rated_shown', 'top_rated_page', 'prev_min_rating',
        'popular_shown', 'popular_page',
        'title_recommendations', 'title_input'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

    st.markdown("""
        ### Welcome!
        This Movie Recommendation App helps you discover great movies.
        Use the sidebar to select how you want to get your recommendations.
    """)
    st.image("https://media.giphy.com/media/xT0BKqhdlKCxCNsVTq/giphy.gif", use_container_width=True)

elif mode == "By Movie Title":
    st.subheader("🔎 Recommend Movies Similar to:")
    movie_input = st.text_input("Enter a movie name")
    if st.button("Recommend"):
        st.info(f"Showing recommendations for: **{movie_input}**")
        results = recommend_by_title(movies, movie_input)
        show_movie_cards(results)

# By Genre
elif mode == "By Genre":
    st.subheader("🎭 Browse Top Movies by Genre")
    genre = st.selectbox("Choose a genre", ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi"])

    # Reset page when genre changes
    if 'prev_genre' not in st.session_state or st.session_state.prev_genre != genre:
        st.session_state.genre_page = 0
        st.session_state.prev_genre = genre
        st.session_state.genre_shown = False  # Track if shown or not

    if st.button("Show Top Movies"):
        st.session_state.genre_shown = True
        st.session_state.genre_page = 0  # reset page when show clicked

    if st.session_state.get('genre_shown', False):
        filtered = recommend_by_genre(movies, genre)
        start = st.session_state.genre_page * PAGE_SIZE
        end = start + PAGE_SIZE
        page_data = filtered.iloc[start:end]
        show_movie_cards(page_data)

        if end < len(filtered):
            if st.button("Load More"):
                st.session_state.genre_page += 1


elif mode == "Top Rated Movies":
    st.subheader("⭐ Highest Rated Movies")
    min_rating = st.slider("Minimum Rating", 0.0, 5.0, 4.0, step=0.1)

    # Reset page and shown flag when min_rating changes
    if 'prev_min_rating' not in st.session_state or st.session_state.prev_min_rating != min_rating:
        st.session_state.top_rated_page = 0
        st.session_state.prev_min_rating = min_rating
        st.session_state.top_rated_shown = False

    if st.button("Show"):
        st.session_state.top_rated_shown = True
        st.session_state.top_rated_page = 0

    if st.session_state.get('top_rated_shown', False):
        filtered = get_top_rated(movies, min_rating)
        start = st.session_state.top_rated_page * PAGE_SIZE
        end = start + PAGE_SIZE
        page_data = filtered.iloc[start:end]
        show_movie_cards(page_data)

        if end < len(filtered):
            if st.button("Load More"):
                st.session_state.top_rated_page += 1
elif mode == "Most Popular Movies":
    st.subheader("🔥 Most Popular Movies")

    if st.button("Show"):
        st.session_state.popular_shown = True
        st.session_state.popular_page = 0

    if st.session_state.get('popular_shown', False):
        filtered = get_most_popular(movies)
        start = st.session_state.popular_page * PAGE_SIZE
        end = start + PAGE_SIZE
        page_data = filtered.iloc[start:end]
        show_movie_cards(page_data)

        if end < len(filtered):
            if st.button("Load More"):
                st.session_state.popular_page += 1
