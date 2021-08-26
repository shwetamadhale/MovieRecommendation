from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text = ["London Paris London", "Paris Paris London"]
#using scikit learn to find wordcount
#initialising object form the class
cv = CountVectorizer()

#methods: fit transform
count_matrix = cv.fit_transform(text)	#get vectors

print (count_matrix)

#using cosine similarity bw vectors numeric value
similarity_scores = cosine_similarity(count_matrix)
print (similarity_scores)
