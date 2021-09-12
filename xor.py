from string import ascii_lowercase, ascii_uppercase


def encrypt(message, key):
    cypher = []
    final = []
    for b in message:
        if ascii_lowercase.find(b) != -1 and ascii_uppercase.find(b) == -1:
            cypher1 = alphabet[ascii_lowercase.find(b)]
        elif ascii_lowercase.find(b) == -1 and ascii_uppercase.find(b) != -1:
            cypher1 = ALPHABET[ascii_uppercase.find(b)]
        else:
            cypher1 = b
        cypher.append(cypher1)
    for y in range(0, len(message)):
        semi = int(bin(ord(cypher[y])-96), 2) ^ int(bin(ord(key[y])-96), 2)
        semi = semi + 96
        final.append(chr(semi))
    finalPrint = ''.join(final)
    print(finalPrint)
    myFile = open('final.txt', 'w')
    myFile.write(f'Encrypted message: {finalPrint}')


def decrypt(cypher, key):
    msg = []
    final = []
    for y in range(0, len(cypher)):
        semi = int(bin(ord(cypher[y])-96), 2) ^ int(bin(ord(key[y])-96), 2)
        semi = semi + 96
        msg.append(chr(semi))
    for b in msg:
        if ascii_lowercase.find(b) != -1 and ascii_uppercase.find(b) == -1:
            msg1 = ascii_lowercase[''.join(alphabet).find(b)]
        elif ascii_lowercase.find(b) == -1 and ascii_uppercase.find(b) != -1:
            msg1 = ascii_uppercase[''.join(ALPHABET).find(b)]
        else:
            msg1 = b
        final.append(msg1)
    finalPrint = ''.join(final)
    print(finalPrint)
    myFile = open('final.txt', 'w')
    myFile.write(f'Decrypted message: {finalPrint}')


def starto():
    global alphabet, ALPHABET
    choice = input('Welcome to the fusion between XOr and Shift cypher!''\n''Would you like to (E)ncrypt or (D)ecrypt?''\n''>>').lower()
    message = input('Message: ')
    key = input('Key: ')

    if len(message) < len(key):
        newKey = []
        for i in range(0, len(message)):
            newKey.append(key[i])
        ''.join(str(newKey))
    elif len(message) > len(key):
        newKey = []
        x = 0
        for i in range(0, len(message)):
            newKey.append(key[x])
            if x + 1 == len(key):
                x = 0
            else:
                x += 1
        ''.join((str(newKey)))
    else:
        newKey = key

    alphabet = []
    ALPHABET = []
    for i in ascii_lowercase:
        alphabet.append(i)
        ALPHABET.append(i.upper())
    for c in range(0, len(key)):
        hold = alphabet[0]
        alphabet.pop(0)
        alphabet.append(hold)
        hold = ALPHABET[0]
        ALPHABET.pop(0)
        ALPHABET.append(hold)

    if choice == 'e':
        encrypt(message, newKey)
    elif choice == 'd':
        decrypt(message, newKey)

if __name__ == "__main__" :
    starto()
input()
