


# Embeddings are numerical representations of words, sentences, or other text.

'''computer cannot directly understandd the meaning of :  "cat" "dog""car"
convert them into numbers vector like this 
cat → [0.21, 0.45, 0.78, 0.12]
dog → [0.25, 0.48, 0.75, 0.15]
car → [0.91, 0.12, 0.34, 0.67]

types: word, sentence, document, contextual embeddings
'''

# real world example
'''
Movie 1:
"An action movie about a superhero saving the world."
Movie 2:
"A superhero fights villains to protect humanity."
Movie 3:
"A romantic story about two people falling in love."
'''

# System convert them into embeddings like this 
# Movie 1 → [0.21, 0.82, 0.45, ...]
# Movie 2 → [0.23, 0.79, 0.48, ...]
# Movie 3 → [0.91, 0.12, 0.34, ...]


# if the user search for superhero system can find movies 1 and movie 2

from sklearn.feature_extraction.text import TfidfVectorizer
sentences = [
    "I love machine learning",
    "I love Python programming",
    "Machine learning is interesting"
]

vectorizer = TfidfVectorizer()

embeddings = vectorizer.fit_transform(sentences)

print("Words:")
print(vectorizer.get_feature_names_out())

print("\nEmbeddings:")
print(embeddings.toarray())






# another example 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "How can I reset my password?",
    "I forgot my password",
    "What is the weather today?",
    "How do I change my password?"
]
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(sentences)
similarity = cosine_similarity(embeddings)

print("Similarity Matrix:")
print(similarity)









# Real-World Product Recommendation

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

products = [
    "gaming laptop with powerful processor",
    "gaming computer with graphics card",
    "wireless headphones with noise cancellation",
    "office laptop for students",
    "mechanical gaming keyboard"
]
user_search = "I need a laptop for gaming"
all_text = products + [user_search]
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(all_text)
scores = cosine_similarity(
    vectors[-1],
    vectors[:-1]
)
print("Product Recommendations:\n")
for i, score in enumerate(scores[0]):
    print(products[i], "->", round(score, 2))









# Visualize Embeddings

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

sentences = [
    "I love Python",
    "Python programming is easy",
    "Machine learning is interesting",
    "Deep learning uses neural networks",
    "Football is a popular sport",
    "Basketball is a team sport"
]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences).toarray()

pca = PCA(n_components=2)
points = pca.fit_transform(vectors)
plt.scatter(points[:, 0], points[:, 1])

for i, sentence in enumerate(sentences):
    plt.annotate(sentence, (points[i, 0], points[i, 1]))

plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.title("Text Embeddings")
plt.show()