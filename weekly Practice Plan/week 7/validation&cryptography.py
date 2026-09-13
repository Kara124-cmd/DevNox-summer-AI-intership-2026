


# Input validation means checking the data entered by a user before your program accepts or processes it.

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    if 1 <= age <= 120:
        print("Valid age:", age)
    else:
        print("Age must be between 1 and 120.")
else:
    print("Please enter a number.")



# Validate Password length

password = input("Enter your password: ")

if len(password) >= 8:
    print("Password length is valid.")
else:
    print("Password must contain at least 8 characters.")



# Validate Email 
email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Email format looks valid.")
else:
    print("Invalid email.")









#  basic Caesar-cipher cryptography
'''
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the "shift" or "key". The Caesar Cipher technique is one of the earliest and simplest methods of encryption techniques.'''


# A program that receives a Text (string) and Shift value( integer) and returns the encrypted text. 

#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
text = "ATTACKATONCE"
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))




# Atbash Cipher
# In the Atbash cipher, the alphabet is reversed:

# A Python program to illustrate Atbash Cipher Technique

def encrypt(text):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr(90 - (ord(char) - 65))

        # Encrypt lowercase characters
        elif char.islower():
            result += chr(122 - (ord(char) - 97))

        # Keep spaces and symbols unchanged
        else:
            result += char
    return result

# Check the above function
text = "HELLO WORLD"

print("Text  : " + text)
print("Cipher: " + encrypt(text))



# Caesar Cipher — Decryption
# A Python program to illustrate Caesar Cipher Decryption

def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)

        else:
            result += char

    return result


# Check the above function
text = "EXXEGOEXSRGI"
s = 4

print("Cipher : " + text)
print("Shift  : " + str(s))
print("Text   : " + decrypt(text, s))







# Caesar Cipher — Brute Force
# A Python program to demonstrate Caesar Cipher Brute Force

def decrypt(text, s):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)

        else:
            result += char

    return result
text = "KHOOR"

print("Cipher Text:", text)
print("\nPossible Messages:")

for s in range(26):
    print("Shift", s, ":", decrypt(text, s))






# Vigenère Cipher
# The Vigenère cipher uses a keyword instead of one fixed shift.

# A Python program to illustrate Vigenere Cipher

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





