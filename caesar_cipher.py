import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
             'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    word = ''
    if direction == 'decode':
            shift *= -1
    for letter in text:
        if letter in alphabet:
            idx = alphabet.index(letter)
            new_index = idx + shift
            if new_index > 25:
                new_index = (new_index % 25)-1
            word += alphabet[new_index]
        else:
             word += letter
    print(f"The {direction}d text is {word}")

caesar(text, shift, direction)



