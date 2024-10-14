# Importing necessary modules
# 'random' for shuffling the key and 'string' for accessing common characters like digits, letters, and punctuation.
import random
import string

# Define the character set that will be used for encryption and decryption.
# This includes a space, digits (0-9), punctuation symbols, uppercase and lowercase letters.
chars = " " + string.digits + string.punctuation + string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase
# Convert the character string into a list for easy indexing and manipulation.
chars = list(chars)

# Create a copy of the original character set to generate the encryption key.
key = chars.copy()

# Shuffle the key list to randomize the mapping between original characters and encrypted characters.
random.shuffle(key)

# --------- Encryption Process ---------

# Prompt the user to input the text they want to encrypt.
txt = input("Enter a text: ")

# Initialize an empty string to hold the encrypted text.
cipher_test = ""

# Loop through each character in the input text.
for letter in txt:
    # Find the index of the character in the original character list (chars).
    index = chars.index(letter)
    # Use that index to find the corresponding encrypted character from the shuffled key list.
    cipher_test += key[index]

# Print the encrypted message.
print(f"Encrypted message of '{txt}' is : {cipher_test}")