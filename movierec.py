import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#1 read dataset csv file
#2 feature selection
#3 creating column in dataframe which will combine selected features
#4 creating count matrix from new column
#5 determine cosine similarity based on prev count matrix
#6 input for movie that user likes
#7 index for the input movie title
#8 list similar movies based on similarity score
#9 print the similar movie titles till count 50

#get index for input movie
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

#1 read dataset csv file using pandas

df = pd.read_csv("movie_dataset.csv")
print ('Headers are' , df.head())
print ('Columns of dataset are' , df.columns)

#2 feature selection
features = ['genres','keywords','cast','director']


#3 creating column in dataframe which will combine selected features
for feature in features:			#for NaN error in the method, fills NaNs with empty string
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:		
		return row['genres'] +" "+row['keywords']+" "+row['cast']+" "+row['director']	#combine to a giant string
	except:
		print ("Error:", row)	

df["combined_features"] = df.apply(combine_features,axis=1)		#use above method for entire datframe, axis=1 passes each row individually

print ("Combined Features are ", df["combined_features"].head())

#4 creating count matrix from new column
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])		#vector

#5 determine cosine similarity based on prev count matrix
cosine_sim = cosine_similarity(count_matrix) 				#numeric value for similarity scores

#6 input for movie that user likes
movie_user_likes = "Avengers: Age of Ultron"

#7 index for the input movie title
movie_index = get_index_from_title(movie_user_likes)
		#enumerating list, giving lsit of tuples
similar_movies =  list(enumerate(cosine_sim[movie_index]))

#8 list similar movies based on similarity score
		#sort list of tuples
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

#9 print the similar movie titles till count 50
i=0
for element in sorted_similar_movies:
		print (get_title_from_index(element[0]))
		i=i+1
		if i>50:
			break
