alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# create func called 'encrypt' that takes 'text' & 'shift' as parameters
def encrypt(text, shift):
    encrypted_word = ''
    for i in range(len(text)):
        index_Of_text = alphabet.index(text[i])
        new_index = index_Of_text + shift
        if new_index > 25:
            encrypted_word += alphabet[(new_index % 25)-1]
        else: 
            encrypted_word += alphabet[new_index]
    print(f"The encrypted text is: {encrypted_word}")

# create a func called 'decrypt' that takes 'text' & 'shift' as parameters
def decrypt(text, shift):
    decrypted_word = ''
    for letter in text:
        idx = alphabet.index(letter)
        new_index = idx - shift
        decrypted_word += alphabet[new_index]
    print(f"The decrypted text is: {decrypted_word}")

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)

