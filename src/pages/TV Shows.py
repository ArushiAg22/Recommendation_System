import streamlit as st
import pandas as pd
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.stateful_button import button
from streamlit_js_eval import streamlit_js_eval
import pickle


# extract the new_df dataframe from shows.pkl
shows_list = pickle.load(open("./pickle_files/shows.pkl", "rb"))

# extract the names of shows
shows_list_title = shows_list["name"].values

# extract the similarity which contain our cosine similarity values
cosine_sim = pickle.load(open("./pickle_files/shows_tfidf.pkl", "rb"))
indices = pd.Series(shows_list.index, index=shows_list['name']).drop_duplicates()

st.header('''**TV Shows Recommendation System**''')


@st.cache_data
def get_recommendations(title):
    # Function that takes in show title as input and outputs most similar shows

    # Get the index of the show that matches the name
    idx = indices[title]

    # Get the pairwise-similarity scores of all shows with that show
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the shows based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 20 most similar shows
    sim_scores = sim_scores[1:21]

    # Get the show indices
    show_indices = [i[0] for i in sim_scores]

    # Get the show titles and join them into separate lines
    recommended_shows = [shows_list['name'].iloc[i] for i in show_indices]

    return recommended_shows


def rec_shows(j, shows):
    # Function to show recommendations
    st.write(shows[j])
    st.write(shows[j+1])
    st.write(shows[j+2])
    st.write(shows[j+3])
    st.write(shows[j+4])


selected_show = selectbox("Please select a TV Show", shows_list_title, no_selection_label="Select")

# to change session state of buttons if no movie is selected (Useful after 1st run)
if selected_show is None:
    st.session_state["rec_tv"] = False
    st.session_state["more1_tv"] = False
    st.session_state["more2_tv"] = False
    st.session_state["more3_tv"] = False

rec_button = button("Show Recommendations", key="rec_tv")
if rec_button:
    st.write("Recommended Shows:\n")
    shows = get_recommendations(selected_show)
    rec_shows(0, shows)
    more_button_1 = button("Show more recommendations!", key="more1_tv")
    if more_button_1:
        rec_shows(5, shows)
        more_button_2 = button("Show more recommendations!!", key="more2_tv")
        if more_button_2:
            rec_shows(10, shows)
            more_button_3 = button("Show more recommendations!!!", key="more3_tv")
            if more_button_3:
                rec_shows(15, shows)
    new = st.button("Select a new TV show")
    if new:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
