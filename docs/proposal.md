## 1. Title and Author

- Project Title: Recommendation System
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name: Arushi Agarwal
- Link to the author's GitHub profile: https://github.com/ArushiAg22
- Link to the author's LinkedIn progile: https://www.linkedin.com/in/arushi-agarwal/
- Link to your PowerPoint presentation file: TBD
- Link to your YouTube video: TBD
    
## 2. Background

### What is it about?
In the age of digital content consumption, the vast array of movies, shows, and books available can be overwhelming for users. With thousands of movies, shows and books being released each year, it has become increasingly challenging for viewers to discover films that align with their preferences and interests. This issue is exacerbated by the proliferation of streaming platforms, which offer extensive libraries of movies and TV shows, making it difficult for users to navigate and choose what to watch. Moreover, these platforms just recommend the movies that they host on their websites which means either the user has to go to each streaming platform to look for their preferred movie or go ahead with the recommendation of that particular platform. To address this problem and enhance the user experience, I propose the development of a Recommendation System for Movies, TV Shows and Books.

This capstone project aims to develop a Recommendation System that provides personalized recommendations to users based on their selection. This system will leverage the power of machine learning algorithms, data analysis and natural language processing techniques, to offer users a tailored list of the top 5 recommendations they are likely to enjoy after selecting a particular movie, TV show or book. our goal is to create an innovative solution that revolutionizes how users interact with digital content, making their entertainment and reading experiences more personalized and enjoyable.

### Why does it matter?

The Recommendation System is significant for several reasons:

**Enhanced User Experience:** A personalized recommendation system ensures that users discover content that aligns with their interests, leading to a more satisfying and engaging experience.

**Increased Engagement:** A well-executed recommendation system can boost user engagement and retention on the platforms, leading to increased user satisfaction and loyalty.

**Revenue Generation:** For platforms offering digital content, personalized recommendations can lead to increased content consumption, directly impacting revenue generation through subscriptions, purchases, or advertisements.

**Content Discovery:** The entertainment industry benefits from users exploring a wider range of content. This can help lesser-known movies, TV shows and books gain visibility and improve the diversity of content consumption.

### What are your research questions?

This project will focus on answering the following research questions:

1. How can we collect and preprocess movie, TV show and Books data for building a recommendation system?
2. How can content features such as genre, keywords, metadata, and textual descriptions be effectively extracted and utilized to create accurate item profiles for movies, shows, and books?
3. How can natural language processing (NLP) and text analysis be leveraged to analyze textual content descriptions and summaries for better content matching in recommendation systems?
4. Which recommendation algorithm(s) will be most suitable for our Recommendation System?

## 3. Data 

Describe the datasets you are using to answer your research questions.

I am using 3 datasets here-

### Dataset 1

- Data sources: Movies Daily Update Dataset [Link](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies)
- Data size: 350 MB
- Data shape: 722710 rows and 20 columns
- Time period: 1970 to 2023
- **What does each row represent?**: A movie
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

**original_language:** There are 167 languages but I will just select movies which are in English

**genres:** There are more than 10000 combinations of different 19 different genres

#### Which variable/column will be your target/label in your ML model?

This is unsupervised learning model

#### Which variables/columns may be selected as features/predictors for your ML models?

title, genres, overview, tagline, keywords

### Dataset 2

- Data sources: TV Series Dataset [Link](https://www.kaggle.com/datasets/bourdier/all-tv-series-details-dataset/data)
- Data size: 250 MB
- Data shape: 152970 rows and 188 columns
- Time period: Till 2023
- **What does each row represent?**: A TV show
- Data dictionary

There are more than 188 columns so I will just mention main ones.

| #  | Column                                   | Dtype   | Definition                          |
|----|------------------------------------------|---------|-------------------------------------|
| 0  | id                                       | int64   | Id of the Show                      |
| 1  | name                                     | object  | Show title                          |
| 2  | original_name                            | object  | Original name of the Show           |
| 3  | overview                                 | object  | Summary of the Show                 |
| 4  | tagline                                  | object  | Tagline of the Show                 |
| 5  | in_production                            | object  | If it is in-production or not       |
| 6  | status                                   | object  | Status of the Show                  |
| 7  | original_language                        | object  | Original language of the Show       |
| 8  | origin_country[0]                        | object  | Original country of the Show        |
| 9  | first_air_date                           | object  | Date pilot was released             |
| 10 | last_air_date                            | object  | Date last episode was released      |
| 11 | number_of_episodes                       | int64   | Total no. of episodes               |
| 12 | number_of_seasons                        | int64   | No. of Seasons                      |
| 13 | poster_path                              | object  | Link to the Show poster             |
| 14 | genres[0].name                           | object  | Genre of the show                   |
| 15 | vote_average                             | float64 | Average of votes received           |
| 16 | vote_count                               | int64   | Total votes received                |
| 17 | created_by[0].name                       | object  | Creator's name                      |
| 18 | production_companies[0].name             | object  | Production company name             |
| 19 | production_companies[0].origin_country   | object  | Country of Production company       |

#### Potential values (for categorical valuables, what are the categories?)

**in_production:** True, False

**status:** Returning Series, Planned, In Production, Pilot, Canceled, Ended

**original_language:** There are 105 languages but I will just select Shows which are in English

**genres:** There are more than 800 combinations of 23 different genres

#### Which variable/column will be your target/label in your ML model?

This is unsupervised learning model

#### Which variables/columns may be selected as features/predictors for your ML models?

name, genres, original_language, overview, tagline, created_by

### Dataset 3

- Data sources: Best Books (10k) Multi-Genre Data [Link](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)
- Data size: 11.75 MB
- Data shape: 10000 rows and 8 columns
- Time period: Till 2023
- **What does each row represent?**: A book
- Data dictionary
 
| #  | Column            | Dtype   | Definition                             |
|----|-------------------|---------|----------------------------------------|
| 0  | Book              | object  | Name of the Book                       |
| 1  | Author            | object  | Author's Name                          |
| 2  | Description       | object  | Summary of the Book                    |
| 3  | Genres            | object  | List of Genres of that Book            |
| 4  | Avg_Rating        | float64 | Average of Ratings received            |
| 5  | Num_Ratings       | object  | Total no. of Ratings received          |
| 6  | URL               | object  | URL to that book on GoodReads website  |

#### Potential values (for categorical valuables, what are the categories?)

**genres:** There are more than 8000 combinations of more than 20 different genres

#### Which variable/column will be your target/label in your ML model?

This is unsupervised learning model

#### Which variables/columns may be selected as features/predictors for your ML models?

Book, Author, Description, Genres

## 4. Exploratory Data Analysis (EDA)

### Dataset 1
#### Data Cleaning
1. Dropped 'backdrop_path' and 'recommendations' columns since I don't need them.
2. Removed duplicate rows
3. Removed rows where title was missing
4. Dropped the rows where Movie was not in English Language
5. Removed Rows where genres and overview both were not there since they both are the main features
6. Filled missing values with "" as I don't want to hinder the result by adding specific word
7. Sanity check for numerical variables

#### EDA




#### Data Preparation
1. Dropped the movies which are not Released.
2. Dropped the movies that were released before 1970
3. Dropped the movies with 20 or lesser votes since we want to recommend movies that have got atleast some votes.
4. Replaced "-" with " " in geners, keyword, credits column
5. Created Tags column which is a combination of Overview, genres, credits, keywords and tagline columns.
6. Words in Tags column in converted into lower case
7. Stemming is done for Tags Column so that we can further implement Content-based recommendation algorithms.

### Dataset 2





### Dataset 3
