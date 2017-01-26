def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value = 0
    for i in alphabet:
        if i != letter.lower() and i != letter.upper():
            value += 1
        if i == letter.lower() or i == letter.upper():
            break
    return value

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newChar = ""
    if char.isalpha() == True:
        pos = alphabet_position(char)
        if pos < 26:
            rotated = pos + rot
        if rotated >= 26:
            rotated %= 26
        if char in alphabet1:
            for char in alphabet1:
                if char == alphabet1[rotated]:
                    newChar += char
        elif char in alphabet:
            for char in alphabet:
                if char == alphabet[rotated]:
                    newChar += char
    else:
        newChar += char
    return newChar

def encrypt(message, rot):
    string = ""
    for char in message:
        rotate = rotate_character(char, rot)
        string += rotate

    return "Your cipher is: " + string
