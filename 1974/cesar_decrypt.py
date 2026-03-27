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
text = "BPZMM IAAQAB AMBBTM ZIKKWWV"
for s in range(26):
    print ("Text  : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + encrypt(text,s))