# MPA Classification using Plot

This project aims to classify movies into different ratings based on their plots. The ratings are based on the **Motion Picture Association (MPA) film rating system**, which is used in the United States and its territories to rate a motion picture's suitability for certain audiences based on its content. The ratings are:

- G – General Audiences
- PG – Parental Guidance Suggested
- PG-13 – Parents Strongly Cautioned
- R – Restricted

The project uses natural language processing techniques such as **text preprocessing**, **feature extraction**, **dimensionality reduction**, and **machine learning algorithms** to analyze the plot summaries of movies and predict their ratings.

## Data

The data for this project comes from one source:

- The [IMDb website](https://www.imdb.com/), which provides the plot summaries and other metadata for movies.

The data was scraped using Python scripts and stored in CSV files. The final dataset contains more than 10,000 movies with their titles, plots, ratings, genres, release years, and content descriptors.

## Methodology

The methodology for this project consists of four main steps:

1. Data collecting: This step involves crawling the imdb and collecting the dataset, removing any missing or invalid values from it, and standardizing the format of the ratings and content descriptors.
2. Text preprocessing: This step involves transforming the plot summaries into numerical vectors that can be used by machine learning algorithms. This includes removing stopwords, punctuation, etc using nltk.
4. Model training and evaluation: This step involves splitting the data into training and test sets,
applying diffrent types of machine learning algorithm based on BERT (Bidirectional Encoder Representations from Transformers),
a state-of-the-art natural language processing model that can capture both left and right context of a word;
tuning its hyperparameters using grid search method;
comparing its performance using accuracy scores;
and testing it on new data.

## Conclusion

This project demonstrates that it is possible to classify movies into different ratings based on their plots using natural language processing techniques and machine learning algorithms. The results show that some genres and content descriptors are more indicative of certain ratings than others. However,
there are also some limitations and challenges that need to be addressed in future work:

- The dataset is imbalanced with more movies rated R than other ratings. This may affect the performance of some algorithms or introduce bias in the predictions.
- The plot summaries may not capture all aspects of a movie's content that influence its rating such as visual effects,
sound effects,
dialogue,
etc.
A more comprehensive analysis would require additional data sources such as scripts,
reviews,
or trailers.
-The NC-17 rating was not covered by this project due to its rarity and difficulty to predict based on plot summaries alone. A different classification scheme or a larger dataset may be needed to include this rating in future work.
