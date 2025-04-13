text = 'hello world'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
space = ''
for char in text:
    if char == ' ':
        space += char
    else:
        index = alphabet.find(char)
        new_index = index + shift
        space += alphabet[new_index]
        print(f'decrypted text:{text}    encrypted text:{space}')
