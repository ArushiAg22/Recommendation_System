# CAPSTONE PROJECT

## 1. Proposal Title: Recommendation System (Recommendations for Movies, TV Shows and Books)

- **Author Name: Arushi Agarwal**
  
- **Semester: Fall 2023**
  
- **Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang**

- [![GitHub](https://img.shields.io/badge/GitHub-brown?style=flat&logo=github&logoColor=white)](https://github.com/ArushiAg22)
  
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arushi-agarwal/)
  
- Link to PowerPoint presentation file: [Presentation](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/docs/capstone.pptx)
  
- Link to YouTube video: [![Youtube](https://img.shields.io/badge/YouTube-red?style=flat&logo=youtube&logoColor=white)](https://youtu.be/m0PdTbXShV8)
    
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
Before creating the model, it is important to understand our data. I did that in 3 steps for each dataset- Data Cleaning, EDA, Data Pre-Processing.

### Dataset 1
#### Data Cleaning
1. Dropped 'backdrop_path' and 'recommendations' columns since I don't need them.
2. Removed duplicate rows
3. Removed rows where title was missing
4. Dropped the rows where Movie was not in English Language
5. Removed Rows where genres and overview both were not there since they both are the main features
6. Filled missing values with "" as I don't want to hinder the result by adding specific word
7. Sanity check for numerical variables was done

#### EDA
Bar plot for Movie Genres
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Movies_genres.png)
Through this plot, we can see that the dataset contains movies from all genres.

Plt for Movie Release Years
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Movie_year.png)
This plot shows that this dataset contains movies from 1896 to 2023. After looking at this plot, I decided to consider movies which were released after 1970.

Pie Chart for Movie Status
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Movie_status.png)
This plot shows that movies fall under 1 of the 6 status categories. After looking at this plot, I decided to consider movies which have already released.

#### Data Preparation
1. Dropped the movies which are not yet Released.
2. Dropped the movies that were released before 1970
3. Dropped the movies with 20 or lesser votes since we want to recommend movies that have got atleast some votes.
4. Replaced "-" with " " in geners, keyword, credits column
5. Created Tags column which is a combination of overview, genres, credits, keywords and tagline columns.
6. Words in Tags column in converted into lower case
7. Stemming is done for Tags Column so that we can further implement Content-based recommendation algorithms.

### Dataset 2
#### Data Cleaning
1. Removed duplicate rows
2. Removed rows where name of the show was missing
3. Dropped the rows where Movie was not in English Language
4. Since there are 188 columns, I dropped columns that were ot needed. After this step, we were left with 33 columns only.  
5. Dropped rows where genres or created_by was empty
6. Each genre of the show was given in single column so I created a new column called genres by combining all these genres columns.
7. Each creator of the show was given in single column so I created a new column called created_by by combining all these created_by columns.
8. Filled missing values with "" as I don't want to hinder the result by adding specific word
9. Sanity check for numerical variables was done

#### EDA
Bar plot for Show Genres
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Show_genres.png)
Through this plot, we can see that the dataset contains shows from all genre types mostly Comedy and Drama.

Pie Chart for Show Status
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Show_status.png)
This plot shows that shows fall under 1 of the 6 status categories. After looking at this plot, I decided to consider shows whose atleast Pilot has been released.

#### Data Preparation
1. Dropped the shows whose Pilot atleast has been released.
2. Created Tags column which is a combination of overview, genres, created_by and tagline columns.
6. Words in Tags column in converted into lower case
7. Stemming is done for Tags Column so that we can further implement Content-based recommendation algorithms.

### Dataset 3
#### Data Cleaning
1. Dropped 'Unnamed: 0' column.
2. Check if there were any duplicate rows.
3. Removed rows where name of the book was duplicate.
4. Genres were given as a list. This column was converted into " " separated string.
5. Num_Rating column was converted into integer type.
6. Filled missing values with "" as I don't want to hinder the result by adding specific word
8. Sanity check for numerical variables was done.

#### EDA
Bar plot for Show Genres
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Book_genres.png)
This dataset contains books with more than 20 genres. Here I have created a plot for top 20 genres. Fiction is the most common genre.

Bar Plot for top 20 authors
![image](https://github.com/DATA-606-2023-FALL-TUESDAY/Agarwal_Arushi/blob/main/data/Plots/Book_authors.png)
This plot shows that this dataset contains around 38 books by William Shakespeare.

#### Data Preparation
1. Created Tags column which is a combination of Description, Genres and Author columns.
2. Words in Tags column in converted into lower case
3. Stemming is done for Tags Column so that we can further implement Content-based recommendation algorithms.

## 5. Model Training 

- What models you will be using for predictive analytics?

  I am using 2 techniques here- Count Vectorization and TF-IDF (Term Frequency-Inverse Document Frequency)

  Count Vectorization is a technique used to convert a collection of textual data (such as summary, genres) into numerical vectors. It works by counting how many times each word appears.

  TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. TF-IDF gives importance to words based on how often they appear in a document but not too commonly across all documents. It's like finding the unique words in a document.

- How will you train the models?
  - I am using Cosine Similarity to train the models. Since it is recommendation system, we don't train and test data
  - Python packages used - NLTK, PorterStemmer, CountVectorizer, cosine_similarity, TfidfVectorizer, linear_kernel
  - The development environments includes - Personal Laptop, Jupyter Notebook and PyCharm
- How will you measure and compare the performance of the models?
  
  For the current phase of the project, I am manually evaluating the recommendations to assess their relevance and coherence. This hands-on approach allows me to intuitively gauge if the suggestions align with users' selections.

## 6. Application of the Trained Models
I have used Streamlit to create an interactive web app for this Recommendation system.

## 7. Conclusion
In summary, this project focused on developing a content-based recommendation system for movies, shows, and books. By leveraging techniques like Count Vectorization and TF-IDF, I was able to convert textual data into numerical representations, enabling the system to suggest relevant items to users based on their selection.

#### Potential Applications:

The developed recommendation system has the potential to enhance user experiences on platforms offering movies, shows, and books. It can be integrated into streaming services, online bookstores, and media platforms to provide personalized content suggestions tailored to individual tastes.

#### Limitations:

Despite the progress made, there are limitations to this work. The system relies heavily on the quality and quantity of textual data available. Incomplete or biased datasets may affect the accuracy of recommendations. Additionally, the system does not consider user interactions or feedback, which could further enhance recommendation accuracy.

#### Lessons Learned:

Throughout the project, valuable lessons were learned about the challenges in natural language processing, including the nuances of text representation and the importance of understanding user context. The importance of quality data became evident. Ensuring completeness and lack of bias in the dataset is fundamental for accurate recommendations. The iterative nature of system development taught the value of continuous refinement and adaptation to changing requirements. Recognizing the dynamic nature of user preferences highlighted the necessity for flexible algorithms.

#### Future Research Directions:

As a future step, conducting in-depth research on advanced evaluation techniques could provide deeper insights into the system's performance. Deploying user surveys and feedback forms will enable us to gather direct opinions from users, shaping our understanding of their experiences and preferences. Exploring quantitative metrics, such as Click-Through Rate (CTR), would offer a data-driven perspective on user engagement. It is important to keep an eye on emerging research in the field, as new methods for evaluating recommendation systems are continually being developed. Leveraging a combination of qualitative and quantitative approaches will help in creating a more comprehensive evaluation strategy for the future.

## 8. References
1. Blackwood, Zachary. Switch page function. https://arnaudmiribel.github.io/streamlit-extras/extras/switch_page_button/
2. Blackwood, Zachary. Stateful Button. https://arnaudmiribel.github.io/streamlit-extras/extras/stateful_button/
4. Sharma, Aditya(May 2020). Beginner Tutorial: Recommender Systems in Python. https://www.datacamp.com/tutorial/recommender-systems-python
