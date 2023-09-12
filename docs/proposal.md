## 1. Title and Author

- Project Title: Recommendation System for Movies
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name: Arushi Agarwal
- Link to the author's GitHub profile: https://github.com/ArushiAg22
- Link to the author's LinkedIn progile: https://www.linkedin.com/in/arushi-agarwal/
- Link to your PowerPoint presentation file: TBD
- Link to your YouTube video: TBD
    
## 2. Background

### What is it about?
In today's digital age, the entertainment industry has witnessed an explosion of content production, particularly in the realm of movies. With thousands of movies being released each year, it has become increasingly challenging for viewers to discover films that align with their preferences and interests. This issue is exacerbated by the proliferation of streaming platforms, which offer extensive libraries of movies and TV shows, making it difficult for users to navigate and choose what to watch. Moreover these platforms just recommend the movies that they host on their websites which means either the user has to go to each streaming platform to look for their preferred movie or go ahead with the recommendation of that particular platform. To address this problem and enhance the user experience, I propose the development of a Movie Recommendation System.

This capstone project aims to develop a Movie Recommendation System that provides personalized movie recommendations to users based on their selected movie. This system will leverage the power of machine learning and data analysis to offer users a tailored list of the top 5 movies they are likely to enjoy after selecting a particular movie.

### Why does it matter?

The Movie Recommendation System is significant for several reasons:

**Enhanced User Experience:** By offering personalized movie recommendations, we can improve the overall user experience on movie streaming platforms. Users will spend less time searching for movies and more time enjoying them.

**Increased Engagement:** A well-executed recommendation system can boost user engagement and retention on streaming platforms, leading to increased user satisfaction and loyalty.

**Revenue Generation:** Streaming platforms often rely on user engagement to generate revenue through subscriptions and advertisements. A successful recommendation system can drive more users to these platforms.

**Content Discovery:** The movie industry benefits from users exploring a wider range of films. This can help lesser-known movies gain visibility and improve the diversity of content consumption.

### What are your research questions?

This project will focus on answering the following research questions:

1. How can we collect and preprocess movie data for building a recommendation system?
2. Which recommendation algorithm(s) will be most suitable for our Movie Recommendation System?
3. What impact does the availability of metadata (e.g., movie descriptions, cast, crew) have on recommendation accuracy?
4. What are the implications of implementing a hybrid recommendation system that combines collaborative filtering and content-based approaches?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data sources: Movies Daily Update Dataset [Link](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies)
- Data size: 350 MB
- Data shape (# of rows and # columns): 722710 rows and 20 columns
- Time period (for example, 2010 to 2020) if your data are time-bound: Till 2023
- **What does each row represent?(a patient, a school, a crime, etc.)**: Each row represents a movie
- Data dictionary
 
| #  | Column               | Dtype   | Definition                          |
|----|----------------------|---------|-------------------------------------|
| 0  | id                   | int64   | Id of the Movie                     |
| 1  | title                | object  | Movie title                         |
| 2  | genres               | object  | Movie genres                        |
| 3  | original_language    | object  | Movie language                      |
| 4  | overview             | object  | Summary of the movie                |
| 5  | popularity           | float64 | Popularity of the movie             |
| 6  | production_companies | object  | Movie production companies names    |
| 7  | release_date         | object  | Movie release date                  |
| 8  | budget               | float64 | Budget of the movie                 |
| 9  | revenue              | float64 | Revenue that movie generated        |
| 10 | runtime              | float64 | Runtime of the movie                |
| 11 | status               | object  | Status of the movie                 |
| 12 | tagline              | object  | Movie tagline                       |
| 13 | vote_average         | float64 | Average of votes received on TMDB   |
| 14 | vote_count           | float64 | Total no. of votes received on TMDB |
| 15 | credits              | object  | Movie cast                          |
| 16 | keywords             | object  | Keywords for the movie              |
| 17 | poster_path          | object  | Link to the movie poster            |
| 18 | backdrop_path        | object  | Link to the movie backdrop          |
| 19 | recommendations      | object  | Ids of recommended movies           |

#### Potential values (for categorical valuables, what are the categories?)

**status:** Released, Planned, In Production, Post Production, Canceled, Rumored

**original_language:** There are 167 categories

**genres:** There are more than 10000 combinations of different genres which might get divided into separate columns on later stage

#### Which variable/column will be your target/label in your ML model?

This is unsupervised learning model

#### Which variables/columns may be selected as features/predictors for your ML models?

title, genres, original_language, overview, tagline, keywords
