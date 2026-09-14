
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

