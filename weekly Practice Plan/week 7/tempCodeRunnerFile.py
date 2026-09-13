
def encrypt(text, key):
    result = ""
    key = key.upper()

    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index]) - 65

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

            key_index += 1

            # Repeat the key
            key_index = key_index % len(key)

        else:
            result += char

    return result
text = "ATTACKATONCE"
key = "LEMON"

print("Text  : " + text)
print("Key   : " + key)
print("Cipher: " + encrypt(text, key))