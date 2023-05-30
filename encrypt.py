def encrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

name = input("Enter your name: ")
roll_no = input("Enter roll number: ")
shift = int(roll_no) % 26

text = name + " " + roll_no
print("Original string:", text)
print("After encryption:", encrypt(text, shift))
