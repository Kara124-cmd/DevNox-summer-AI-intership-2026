

'''
Tokenization is a fundamental step in Natural Language Processing (NLP). It involves dividing a Textual input into smaller units known as tokens. These tokens can be in the form of words, characters, sub-words or sentences. It helps in improving interpretability of text by different models.
e.g :    "I love machine learning."  can converted to : ["I", "love", "machine", "learning", "."]
'''





'''
Types of Tokenization
1. Word Tokenization
The text is divided into individual words.

Example:
"I am learning Python"
Result:
["I", "am", "learning", "Python"]

Used for: basic NLP tasks, text classification, sentiment analysis.
'''

text = "I love machine learning"

words = text.split()

print("Word Tokens:")
print(words)






'''
2. Sentence Tokenization
A paragraph is divided into individual sentences.

Example:
"Python is easy. Machine learning is interesting."

Result:
[
    "Python is easy.",
    "Machine learning is interesting."
]
'''
import re

text = "Python is easy to learn. Machine learning is interesting. I love programming!"

sentences = re.split(r'[.!?]+', text)

# Remove empty spaces
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

print("Sentence Tokens:")
print(sentences)






'''
3. Character Tokenization
The text is divided into individual characters.

Example:
"Hello"
Result:
["H", "e", "l", "l", "o"]

Advantage: Can handle unknown or misspelled words.
Disadvantage: Creates many tokens.
'''

text = "Hello"

characters = list(text)

print("Character Tokens:")
print(characters)






'''
4. Subword Tokenization
Words are divided into smaller meaningful pieces.

Example:
"unhappiness"

Could become:
["un", "happiness"]
or:
["un", "happy", "ness"]

This method is commonly used by modern NLP models such as BERT, GPT, and other Transformer models.'''

import wordninja

text = "machinelearning"

tokens = wordninja.split(text)

print("Subword Tokens:")
print(tokens)






'''
5. Whitespace Tokenization
Text is split wherever there is a space.

Example:
"I love Python programming"

Result:
["I", "love", "Python", "programming"]

It is one of the simplest types of tokenization.'''

text = "I am learning Python"

tokens = text.split(" ")

print("Whitespace Tokens:")
print(tokens)







# Tokenization complete program

import re

text = "Python is easy. I love Python programming!"

# 1. Word Tokenization
words = text.split()

print("1. Word Tokenization:")
print(words)


# 2. Sentence Tokenization
sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

print("\n2. Sentence Tokenization:")
print(sentences)


# 3. Character Tokenization
characters = list("Python")

print("\n3. Character Tokenization:")
print(characters)


# 4. Whitespace Tokenization
whitespace_tokens = text.split()

print("\n4. Whitespace Tokenization:")
print(whitespace_tokens)


# 5. Subword Tokenization
word = "unhappy"

if word.startswith("un"):
    subwords = ["un", "happy"]
else:
    subwords = [word]

print("\n5. Subword Tokenization:")
print(subwords)


# 6. Punctuation Tokenization
punctuation_tokens = re.findall(r'\w+|[^\w\s]', text)

print("\n6. Punctuation Tokenization:")
print(punctuation_tokens)





