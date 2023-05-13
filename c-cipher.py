# This program encodes and decodes information by shifting the letters of each word

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '?', ',']
length = len(abc)

# this funtion encodes by looking for a character in 'abc' and replaces it with abc[character+key]
def encoder(key = 3):
    encoded = []
    message = input('Enter your message here: \n')
    message = message.upper()
    for character in message:
        if character in abc:
            number = abc.index(character) + key
            if number >= length:
                number -= length
            encoded.append(abc[number])
        else:
            encoded.append(character) 

    for i in encoded:
        print(i, end="")

# this funtion decodes by looking for a character in 'abc' and replaces it with abc[character-key]
def decoder(key = 3):
    decoded = []
    message = input('Enter your message here: \n')
    message = message.upper()
    for character in message:
        if character in abc:
            number = abc.index(character) - key
            if number >= length:
                number -= length
            decoded.append(abc[number])
        else:
            decoded.append(character) 

    for i in decoded:
        print(i, end="")


print('Caesar Cipher')

action = input('Do you want to encrypt or decrypt a message? (e/d): ')

# asks for input to create a key
while True:
    try:
        global key
        key = int(input(f'Enter a number between 0 and {length}: \n'))
        if key <= length:
            break
        else:
            a
    except:
        print('Please try again, that was not a valid number')

# checks if the user wants to encrypt or decrypt a message
if action == 'e':   
    encoder()
elif action == 'd':
    decoder()
else:
    print(f'you should write \'e\' or \'d\', without spaces. Instead you typed: {action}')