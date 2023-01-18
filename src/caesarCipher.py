alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encodeCaesarCipher(plainText, key):
    cipherText = ""
    for ch in plainText:
        ordValue = ord(ch)-65
        alphabetIndex = (ordValue - key) % 26
        cipherText += alphabet[(alphabetIndex)]
    return cipherText

def decodeCaesarCipher(cipherText, key):
    plainText = ""
    for ch in cipherText:
        ordValue = ord(ch)-65
        alphabetIndex = (ordValue + key) % 26
        plainText += alphabet[(alphabetIndex)]
    return plainText

def tryDecode(cipherText):
    for key in range(1, 26):
        plainText = decodeCaesarCipher(cipherText, key)
        print("Shift %s: %s" % (key, plainText))

def main():
    cipherTexts = ["NCCYVRQPELCGBYBTL", "ECGUCTEKRJGT"]
    for cipherText in cipherTexts:
        print("Cipher text: %s\n" % cipherText)
        tryDecode(cipherText)
        print()

    for key in [1,2,3,25]:
        print("Cipher text for %s with k=%d:" % ("CYBERSECURITY", key))
        print(encodeCaesarCipher("CYBERSECURITY", key))

if __name__ == "__main__":
    main()