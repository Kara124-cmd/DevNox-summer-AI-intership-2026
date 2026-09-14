
# TASK 1
# Tokenize a paragraph manually, then compare the result to a Hugging Face tokenizer.

from transformers import AutoTokenizer
# Paragraph
text = """
Machine learning is a part of Artificial Intelligence.
It helps computers learn from data and make predictions.
"""

#  MANUAL TOKENIZATION
# Convert paragraph to lowercase
manual_text = text.lower()

# Replace common punctuation with spaces
for symbol in [".", ",", "!", "?", ":", ";"]:
    manual_text = manual_text.replace(symbol, " ")

# Split paragraph into words
manual_tokens = manual_text.split()
print("MANUAL TOKENS:")
print(manual_tokens)
print("\nNumber of manual tokens:", len(manual_tokens))

# HUGGING FACE TOKENIZATION
# Load a pretrained Hugging Face tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the paragraph
hf_tokens = tokenizer.tokenize(text)

print("\nHUGGING FACE TOKENS:")
print(hf_tokens)
print("\nNumber of Hugging Face tokens:", len(hf_tokens))

#  COMPARISON
print("\n--- COMPARISON ---")

print("Manual token count:", len(manual_tokens))
print("Hugging Face token count:", len(hf_tokens))

print("\nManual tokenization:")
print(manual_tokens)
print("\nHugging Face tokenization:")
print(hf_tokens)









# TASK 2
# Run a pretrained sentiment-analysis pipeline on 5 sample sentences and compare outputs.


from transformers import pipeline
# Create a pretrained sentiment-analysis pipeline
sentiment = pipeline("sentiment-analysis")

# 5 sample sentences
sentences = [
    "I really enjoyed this movie.",
    "This product is excellent and very useful.",
    "I am disappointed with the service.",
    "The food was terrible.",
    "The weather is okay today."
]
# Run sentiment analysis
results = sentiment(sentences)
# Display results
print("SENTIMENT ANALYSIS RESULTS")
print("-" * 40)

for sentence, result in zip(sentences, results):
    print("Sentence:", sentence)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 4))
    print()










# TASK 3
# Load and preprocess a small image dataset for a basic computer-vision task.

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10

#  Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

#  Display dataset shape
print("Training images:", X_train.shape)
print("Training labels:", y_train.shape)

print("Testing images:", X_test.shape)
print("Testing labels:", y_test.shape)

#  Use a small part of the dataset
X_train = X_train[:1000]
y_train = y_train[:1000]

X_test = X_test[:200]
y_test = y_test[:200]


print("\nAfter selecting small dataset:")
print("Training images:", X_train.shape)
print("Testing images:", X_test.shape)

#  Normalize images
# Pixel values are originally 0 to 255.
# Convert them to 0 to 1.

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

#  Class names
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

#  Display 5 sample images
plt.figure(figsize=(10, 5))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_train[i])
    # Convert label number to class name
    label = y_train[i][0]
    plt.title(class_names[label])
    plt.axis("off")


plt.tight_layout()
plt.show()

#  Print some information
print("\nPreprocessing completed!")

print("Image size:", X_train[0].shape)

print("Pixel minimum:", X_train.min())
print("Pixel maximum:", X_train.max())









# TASK 5
# Write basic input-validation code that blocks obviously malformed/suspicious input strings.

import re
def validate_input(user_input):

    # Remove extra spaces
    user_input = user_input.strip()

    # Check for empty input
    if user_input == "":
        return False, "Input cannot be empty."

    # Check maximum length
    if len(user_input) > 100:
        return False, "Input is too long."

    # Suspicious patterns
    suspicious_patterns = [
        r"<script",          # Script injection
        r"</script>",        # Script closing tag
        r"javascript:",      # JavaScript injection
        r"onerror\s*=",      # HTML event injection
        r"onload\s*=",       # HTML event injection

        r"'\s*or\s*'1'\s*=\s*'1",  # SQL injection
        r"'\s*or\s*1\s*=\s*1",      # SQL injection
        r"--",               # SQL comment
        r";\s*drop\s+table", # SQL command

        r"\.\./",            # Path traversal
        r"\bunion\s+select\b", # SQL UNION injection
        r"\b(rm\s+-rf|shutdown|format)\b"  # Dangerous commands
    ]
    # Check input against patterns
    for pattern in suspicious_patterns:

        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Suspicious input detected."
    return True, "Input is valid."

# Get input from user
user_input = input("Enter your input: ")
# Validate input
valid, message = validate_input(user_input)

# Display result
if valid:
    print("Accepted:", user_input)
else:
    print("Blocked:", message)








# TASK 6
# Implement a simple Caesar cipher (encrypt and decrypt) to understand basic cryptography.


# Encryption function
def encrypt(text, shift):
    result = ""
    for char in text:

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # Keep numbers, spaces and symbols unchanged
        else:
            result += char
    return result

# Decryption function
def decrypt(text, shift):
    # Decryption is encryption with a negative shift
    return encrypt(text, -shift)

# Get input from user
text = input("Enter your message: ")
# Check empty input
if text.strip() == "":
    print("Error: Message cannot be empty.")

else:
    # Get shift value
    try:
        shift = int(input("Enter shift value (1-25): "))

        # Validate shift
        if shift < 1 or shift > 25:
            print("Error: Shift must be between 1 and 25.")
        else:
            # Encrypt the message
            encrypted = encrypt(text, shift)

            # Decrypt the message
            decrypted = decrypt(encrypted, shift)

            # Display results
            print("\nOriginal Message:", text)
            print("Encrypted Message:", encrypted)
            print("Decrypted Message:", decrypted)
    except ValueError:
        print("Error: Please enter a valid number.")













# MINI PROJECT 
# Security-Aware Text Classifier — build a small spam/phishing-text classifier (NLP) with basic input validation, plus a short write-up of 3 security risks in your own code and how you mitigated them.


# Security-Aware Text Classifier
# Spam / Phishing Text Detection using NLP

import re
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#  Small training dataset
data = {
    "text": [
        "Congratulations! You won a free prize. Click here now.",
        "You have won a $1000 reward. Claim your prize today.",
        "Urgent! Your account has been selected for a free gift.",
        "Click this link to receive your free money.",
        "You are the lucky winner of our cash prize.",
        "Your account will be closed. Verify your information immediately.",
        "Urgent security alert! Click the link to verify your account.",
        "Your password has expired. Login now to avoid suspension.",
        "Congratulations, claim your reward by clicking this link.",
        "You have received a special offer. Act now!",

        "Hello, how are you doing today?",
        "Please send me the project report when you finish.",
        "The meeting will start at 10 AM tomorrow.",
        "Can you help me with my Python assignment?",
        "Your appointment is confirmed for Monday.",
        "Please remember to submit your homework.",
        "The team meeting has been moved to Friday.",
        "I will send the documents this afternoon.",
        "Thank you for your help with the project.",
        "Let's discuss the project tomorrow."
    ],

    "label": [
        "phishing",
        "spam",
        "spam",
        "spam",
        "spam",
        "phishing",
        "phishing",
        "phishing",
        "spam",
        "spam",

        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe"
    ]
}

df = pd.DataFrame(data)

#  Display dataset
print("Dataset:")
print(df)
print("\nNumber of messages:", len(df))

#  Basic text cleaning
def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

df["text"] = df["text"].apply(clean_text)

#  Separate features and labels
X = df["text"]
y = df["label"]

#  Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

#  Convert text into numbers using TF-IDF
vectorizer = TfidfVectorizer(
    max_features=1000,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

#  Train Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)
model.fit(X_train_tfidf, y_train)

#  Test the model
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

#  Input validation
def validate_input(text):

    # Check empty input
    if not text.strip():
        return False, "Input cannot be empty."

    # Check maximum length
    if len(text) > 500:
        return False, "Input is too long. Maximum is 500 characters."

    # Remove control characters
    if any(ord(char) < 32 and char not in "\n\t" for char in text):
        return False, "Invalid control characters detected."

    # Block obvious HTML/script injection
    suspicious_patterns = [
        r"<script\b",
        r"</script>",
        r"javascript:",
        r"onerror\s*=",
        r"onload\s*="
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return False, "Suspicious input detected."
    return True, "Input is valid."

#  Predict a new message
print("\n" + "=" * 50)
print("SECURITY-AWARE TEXT CLASSIFIER")
print("=" * 50)

user_text = input("\nEnter a message to check: ")
# Validate input
valid, message = validate_input(user_text)

if not valid:
    print("\nBLOCKED:", message)

else:
    # Clean input
    cleaned_text = clean_text(user_text)

    # Convert text into TF-IDF features
    user_vector = vectorizer.transform([cleaned_text])

    # Make prediction
    prediction = model.predict(user_vector)[0]

    # Get probability
    probabilities = model.predict_proba(user_vector)[0]

    confidence = max(probabilities) * 100
    # Display result
    print("\nInput:", user_text)
    print("Prediction:", prediction.upper())
    print("Confidence:", round(confidence, 2), "%")


    if prediction == "phishing":
        print("WARNING: This message may be a phishing attempt.")
    elif prediction == "spam":
        print("WARNING: This message may be spam.")
    else:
        print("This message appears to be safe.")

