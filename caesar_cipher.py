alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    word = ''
    for letter in text:
        idx = alphabet.index(letter)
        if direction == 'encode':
            new_index = idx + shift 
            word += alphabet[new_index]
        elif direction == 'decode':
            new_index = idx - shift
            word += alphabet[new_index]
    if direction == 'encode':
        print(f"The encrypted text is: {word}")
    elif direction == 'decode':
        print(f"The decrypted text is: {word}")

caesar(text, shift, direction)



