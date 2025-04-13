text = 'hello world'
custom_key = 'python'
def vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in text:
        if char == ' ':
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message
def encrypt(message, key):
    return vigenere(message, key)
def decrypt(message, key):
    return vigenere(message, key, -1)
print(f'decrypted text: {text}')
decryption = decrypt(text, custom_key)
print(f'\nkey: {custom_key}')
print(f'\nencrypted text: {decryption}')
