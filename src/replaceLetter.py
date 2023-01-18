class Text:
    def __init__(self, text):
        self.text = text

    def replaceLetter(self, oldLetter, newLetter):
        self.text = self.text.replace(oldLetter, newLetter)

    def __str__(self):
        return self.text

def readFile(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def decryptTurkishCipher():
    text = readFile("input/turciphertext.txt")

    text = Text(text)

    # text.replaceLetter("e", "A")
    # text.replaceLetter("n", "F")
    # text.replaceLetter("g", "R")
    # text.replaceLetter("r", "G")
    # text.replaceLetter("y", "T")
    # text.replaceLetter("ğ", "P")
    # text.replaceLetter("l", "I")
    # text.replaceLetter("s", "B")
    # text.replaceLetter("b", "İ")
    # text.replaceLetter("u", "Ğ")
    # text.replaceLetter("ç", "L")
    # text.replaceLetter("m", "E")
    # text.replaceLetter("ı", "Ç")
    # text.replaceLetter("a", "C")
    # text.replaceLetter("f", "M")
    # text.replaceLetter("ö", "N")
    # text.replaceLetter("d", "O")
    # text.replaceLetter("o", "H")
    # text.replaceLetter("t", "D")
    # text.replaceLetter("i", "J")
    # text.replaceLetter("c", "K")
    # text.replaceLetter("j", "S")
    # text.replaceLetter("v", "U")
    # text.replaceLetter("p", "V")
    # text.replaceLetter("z", "Ş")
    # text.replaceLetter("k", "Y")
    # text.replaceLetter("h", "Z")
    # text.replaceLetter("ş", "Ü")
    # text.replaceLetter("ü", "Ö")

    # Plaintext Alphabet     A & B & C & Ç & D & E & F & G & Ğ & H & I & İ & J & K & L & M & N & O & Ö & P & R & S & Ş & T & U & Ü & V & Y & Z
    # Ciphertext Alphabet    E & S & A & I & T & M & N & R & U & O & L & B & İ & C & Ç & F & Ö & D & Ü & Ğ & G & J & Z & Y & V & Ş & P & K & H

    keyMap = {"a": "C", "b": "İ", "c": "K", "ç": "L", "d": "O", "e": "A", "f": "M", "g": "R", "ğ": "P", "h": "Z", "i": "J", "ı": "Ç", "j": "S", "k": "Y", "l": "I", "m": "E", "n": "F", "o": "H", "ö": "N", "p": "V", "r": "G", "s": "B", "ş": "Ü", "t": "D", "u": "Ğ", "ü": "Ö", "v": "U", "y": "T", "z": "Ş"}

    for key in keyMap:
        text.replaceLetter(key, keyMap[key])

    with open("output/turplaintext.txt", "w") as f:
        f.write(str(text))

    print("Turkish Cipher Decrypted:")
    print(text)
    print()

def decryptEnglishCipher():
    text = readFile("input/engciphertext.txt")

    text = Text(text)

    # text.replaceLetter("n", "E")
    # text.replaceLetter("c", "T")
    # text.replaceLetter("q", "X")
    # text.replaceLetter("d", "H")
    # text.replaceLetter("z", "R")
    # text.replaceLetter("i", "C")
    # text.replaceLetter("o", "I")
    # text.replaceLetter("v", "P")
    # text.replaceLetter("x", "Y")
    # text.replaceLetter("h", "S")
    # text.replaceLetter("e", "A")
    # text.replaceLetter("b", "N")
    # text.replaceLetter("t", "L")
    # text.replaceLetter("p", "U")
    # text.replaceLetter("r", "D")
    # text.replaceLetter("k", "G")
    # text.replaceLetter("y", "O")
    # text.replaceLetter("l", "F")
    # text.replaceLetter("s", "M")
    # text.replaceLetter("f", "V")
    # text.replaceLetter("j", "W")
    # text.replaceLetter("g", "Q")
    # text.replaceLetter("u", "K")
    # text.replaceLetter("a", "B")

    keyMap = {"a": "B", "b": "N", "c": "T", "d": "H", "e": "A", "f": "V", "g": "Q", "h": "S", "i": "C", "j": "W", "k": "G", "l": "F", "m": "J", "n": "E", "o": "I", "p": "U", "q": "X", "r": "D", "s": "M", "t": "L", "u": "K", "v": "P", "w": "Z", "x": "Y", "y": "O", "z": "R"}

    for key in keyMap:
        text.replaceLetter(key, keyMap[key])

    with open("output/engplaintext.txt", 'w') as f:
        f.write(str(text))

    print("English Cipher Decrypted:")
    print(text)
    print()


def main():
    decryptTurkishCipher()
    decryptEnglishCipher()

if __name__ == "__main__":
    main()

