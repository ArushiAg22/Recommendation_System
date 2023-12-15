import streamlit as st
import pandas as pd
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.stateful_button import button
from streamlit_js_eval import streamlit_js_eval
import requests
from bs4 import BeautifulSoup
import pickle


# extract the new_df dataframe from books.pkl
books_list = pickle.load(open("./pickle_files/books.pkl", "rb"))

# extract the titles of books
books_list_title = books_list["Book"].values

# extract the similarity which contain our cosine similarity values
cosine_sim = pickle.load(open("./pickle_files/books_tfidf.pkl", "rb"))
indices = pd.Series(books_list.index, index=books_list['Book']).drop_duplicates()

st.header('''**Books Recommendation System**''')


@st.cache_data
def get_recommendations(title):
    # Function that takes in book title as input and outputs most similar books

    # Get the index of the book that matches the title
    idx = indices[title]

    # Get the pairwise-similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 20 most similar books
    sim_scores = sim_scores[1:21]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Get the book titles and join them into separate lines
    recommended_books = [books_list['Book'].iloc[i] for i in book_indices]
    books_link = [books_list['URL'].iloc[i] for i in book_indices]

    return recommended_books, books_link

@st.cache_data
def get_link(url):
    # Function to get book image link given in Goodreads website link of that book

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the image tag using its class name and extract the 'src' attribute
    image_tag = soup.find('img', class_='ResponsiveImage')

    # Extract the 'src' attribute of the image tag to get the image link
    if image_tag:
        image_link = image_tag['src']
        return image_link
    else:
        return "Images/Qo5mfYDE5v-350.png"


def show_books(j, links, books):
    # Function to show recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        img = get_link(links[j])
        st.image(img)
        st.write(books[j])
    with col2:
        img = get_link(links[j+1])
        st.image(img)
        st.write(books[j+1])
    with col3:
        img = get_link(links[j+2])
        st.image(img)
        st.write(books[j+2])
    with col4:
        img = get_link(links[j+3])
        st.image(img)
        st.write(books[j+3])
    with col5:
        img = get_link(links[j+4])
        st.image(img)
        st.write(books[j+4])


selected_book = selectbox("Please select a Book", books_list_title, no_selection_label="Select")

# to change session state of buttons if no movie is selected (Useful after 1st run)
if selected_book is None:
    st.session_state["rec_b"] = False
    st.session_state["more1_b"] = False
    st.session_state["more2_b"] = False
    st.session_state["more3_b"] = False

rec_button = button("Show Recommendations", key="rec_b")
if rec_button:
    st.write("Recommended Books:\n")
    books, links = get_recommendations(selected_book)
    show_books(0, links, books)
    more_button_1 = button("Show more recommendations!", key="more1_b")
    if more_button_1:
        show_books(5, links, books)
        more_button_2 = button("Show more recommendations!!", key="more2_b")
        if more_button_2:
            show_books(10, links, books)
            more_button_3 = button("Show more recommendations!!!", key="more3_b")
            if more_button_3:
                show_books(15, links, books)
    new = st.button("Select a new book")
    if new:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
