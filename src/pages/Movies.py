import streamlit as st
import pandas as pd
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.stateful_button import button
from streamlit_js_eval import streamlit_js_eval
import pickle

# extract the new_df dataframe from movies.pkl
movies_list = pickle.load(open("./pickle_files/movies.pkl", "rb"))

# extract the titles of movies
movies_list_title = movies_list["title"].values

# extract the similarity which contain our cosine similarity values
cosine_sim = pickle.load(open("./pickle_files/movies_tfidf.pkl", "rb"))
indices = pd.Series(movies_list.index, index=movies_list['title']).drop_duplicates()

st.header('''**Movie Recommendation System**''')


@st.cache_data
def get_recommendations(title):
    # Function that takes in movie title as input and outputs most similar movies

    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwise-similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 20 most similar movies
    sim_scores = sim_scores[1:21]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Get the movie titles and join them into separate lines
    recommended_movies = [movies_list['title'].iloc[i] for i in movie_indices]
    movie_posters = [movies_list['img_link'].iloc[i] for i in movie_indices]

    return recommended_movies, movie_posters


def show_movies(j, posters, movies):
    # Function to show recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[j])
        st.write(movies[j])
    with col2:
        st.image(posters[j+1])
        st.write(movies[j+1])
    with col3:
        st.image(posters[j+2])
        st.write(movies[j+2])
    with col4:
        st.image(posters[j+3])
        st.write(movies[j+3])
    with col5:
        st.image(posters[j+4])
        st.write(movies[j+4])

selected_movie = selectbox("Please select a Movie", movies_list_title, no_selection_label="Select")

# to change session state of buttons if no movie is selected (Useful after 1st run)
if selected_movie is None:
    st.session_state["rec_m"] = False
    st.session_state["more1_m"] = False
    st.session_state["more2_m"] = False
    st.session_state["more3_m"] = False

rec_button = button("Show Recommendations", key="rec_m")
if rec_button:
    st.write("Recommended Movies:\n")
    movies, posters = get_recommendations(selected_movie)
    show_movies(0, posters, movies)
    more_button_1 = button("Show more recommendations!", key="more1_m")
    if more_button_1:
        show_movies(5, posters, movies)
        more_button_2 = button("Show more recommendations!!", key="more2_m")
        if more_button_2:
            show_movies(10, posters, movies)
            more_button_3 = button("Show more recommendations!!!", key="more3_m")
            if more_button_3:
                show_movies(15, posters, movies)
    new = st.button("Select a new movie")
    if new:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
