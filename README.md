# Movie Recommendation System Using Cosine Similarity


A Python-based movie recommendation system using text feature extraction and cosine similarity calculation.

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Implementation Steps](#implementation-steps)
- [Example Code](#example-code)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Background
This project implements a movie recommendation system that uses text feature extraction and cosine similarity to suggest similar movies based on genres, keywords, cast, and director.

## Install
To set up the project, clone the repository and install the required dependencies.

```sh
$ git clone https://github.com/your-username/movie-recommender.git
$ cd movie-recommender
$ pip install -r requirements.txt
```

## Usage
1. Ensure you have the dataset (`movie_dataset.csv`) in the project directory.
2. Run the Python script:
   ```sh
   python movierec.py
   ```
3. Enter a movie title to get recommendations.

## Features
- **Text Feature Extraction**: Uses CountVectorizer to transform text data.
- **Cosine Similarity Calculation**: Measures similarity between movies.
- **Movie Recommendation**: Provides movie suggestions based on user input.
- **Data Cleaning & Handling**: Processes missing values and extracts relevant features.

## Technologies Used
- **Python Libraries**: Pandas, NumPy, Scikit-learn
- **Machine Learning**: Cosine Similarity for recommendation
- **Natural Language Processing**: CountVectorizer for feature extraction

## Implementation Steps
1. **Load Data**: Read the movie dataset using Pandas.
2. **Feature Selection**: Extract genres, keywords, cast, and director.
3. **Data Cleaning**: Fill missing values and preprocess text data.
4. **Feature Engineering**:
   - Combine selected features into a single text representation.
   - Convert text into a count matrix.
5. **Similarity Calculation**:
   - Compute cosine similarity between movies.
6. **Recommendation System**:
   - Retrieve movie index based on user input.
   - Sort movies based on similarity scores.
   - Return top recommended movies.

