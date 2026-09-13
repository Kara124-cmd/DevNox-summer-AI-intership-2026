

# Hugging Face is a popular platform and Python library that provides many pretrained AI/NLP models.
# Instead of training a model from zero, we can use an already-trained model.
'''
Pipeline abstraction in Hugging Face is an API that hides the complexities of model inference, allowing us to quick use of pretrained models with minimal setup.
Provides a high-level interface for NLP tasks like text generation, translation, sentiment analysis and many more.
Each pipeline is a configuration of a model, tokenizer and pre/post-processing steps.
It lets you call pipeline() with a task name and handles all internal steps automatically.
Without it, you would need to manually load models, tokenizers, preprocess input and post-process output.
'''

from transformers import pipeline
task_pipeline = pipeline('sentiment-analysis')      # call pipeline function with a task
result = task_pipeline("I love using Hugging Face!")        # providing text for anaylysis
print(result)






# Text Classification (Sentiment Analysis)
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
result = classifier("I recently started reading a great book on data science.")
print(result)






# Named Entity Recognition (NER)
# Identifies named entities in the text such as names of people, organizations, locations, dates, etc.

from transformers import pipeline
ner = pipeline('ner')
result = ner("Statue of Liberty is located in New York.")
print(result)




# Text Generation
from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
result = generator("Once upon a time", max_length=50)
print(result)




# questino anwering
from transformers import pipeline
question_answerer = pipeline('question-answering')
context = "Eiffel tower is located in Paris."
result = question_answerer(question="Where is eiffel tower located?", context=context)
print(result)







# translation 
from transformers import pipeline
translator = pipeline('translation_en_to_fr', model='Helsinki-NLP/opus-mt-en-fr')
result = translator("Hello, how are you?")
print(result)





# summarization 
from transformers import pipeline
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
result = summarizer("The weather today is quite pleasant with a gentle breeze and clear skies. The temperature is comfortably mild, hovering around 22°C, making it a perfect day to spend time outdoors. The sun is shining brightly, but the cool wind provides a refreshing break from the warmth. It's a great day for a walk in the park or enjoying a coffee on the patio. As the day progresses, the skies are expected to remain clear, and temperatures are likely to stay moderate throughout the afternoon.", max_length=25)
print(result)





#multiple sentences
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
texts = [
    "I love this phone.",
    "The product is terrible.",
    "The service was excellent.",
    "I am disappointed with the delivery."
]
results = classifier(texts)
for text, result in zip(texts, results):
    print(text)
    print(result)
    print()






# customer review system
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")
reviews = [
    "The phone is amazing and the battery is excellent.",
    "The delivery was very late and the product was damaged.",
    "I am very happy with my purchase.",
    "The quality is poor and I am disappointed."
]

results = sentiment(reviews)

print("Customer Review Analysis")
print("------------------------")

for review, result in zip(reviews, results):
    print("Review:", review)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 3))
    print()