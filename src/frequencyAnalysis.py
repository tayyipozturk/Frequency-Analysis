englishAlphabet = "abcdefghijklmnopqrstuvwxyz"
turkishAlphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def countLetter(filename, letter):
    file = open(filename, "r")
    text = file.read()
    file.close()
    return text.count(letter)

def getStatistics(filename):
    outName = "output/" + filename[6:-4] + "_letter_stats.txt"
    outFile = open(outName, "w")
    dictionary = {}
    totalCount = 0

    if filename[6:9] == "eng":
        for letter in englishAlphabet:
            count = countLetter(filename, letter)
            dictionary[letter] = count
            totalCount += count
    else:
        for letter in turkishAlphabet:
            count = countLetter(filename, letter)
            dictionary[letter] = count
            totalCount += count

    sortedDictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    outFile.write("Frequency ratio for " + filename[6:-4] + ":\n")
    for key, value in sortedDictionary:
        try:
            outFile.write(key + " " + str(round(value/totalCount*100, 2)) + "%\t Occurrences: " + str(value) + "\n")
        except:
            outFile.write(str(key.encode("utf-8")) + str(round(value/totalCount*100, 2)) + "%\t Occurrences: " + str(value) + "\n")
    outFile.close()

def getNgram(filename,n):
    file = open(filename, "r")
    outName = "output/" + filename[6:-4]+"_ngrams/" + filename[6:-4] + "_" + str(n) + "gram.txt"
    text = file.read()
    totalCount = 0

    ngram = {}
    for i in range(len(text)-n+1):
        ngram[text[i:i+n]] = ngram.get(text[i:i+n], 0) + 1
        totalCount += 1
    sortedNgram = sorted(ngram.items(), key=lambda x: x[1], reverse=True)
    outFile = open(outName, "w")
    outFile.write("Frequency ratio for " + filename[6:-4] + " " + str(n) + " grams:\n")
    for key, value in sortedNgram:
        occurrences = value
        value = round(value/totalCount*100, 2)
        outFile.write(key + " " + str(value) + "\t Occurrences:" + str(occurrences) + "\n")
    outFile.close()
    return text

def getDoubles(filename):
    outFile = open("output/" + filename[6:-4] + "_doubles.txt", "w")
    file = open(filename, "r")
    text = file.read()
    doubles = {}
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            doubles[text[i]+text[i]] = doubles.get(text[i]+text[i], 0) + 1
    sortedDoubles = sorted(doubles.items(), key=lambda x: x[1], reverse=True)
    for key, value in sortedDoubles:
        outFile.write(key + " " + str(value) + "\n")


def main():
    getStatistics("input/engciphertext.txt")
    getStatistics("input/turciphertext.txt")
    for n in range(2, 5):
        getNgram("input/engciphertext.txt", n)
        getNgram("input/turciphertext.txt", n)

    getDoubles("input/engciphertext.txt")
    getDoubles("input/turciphertext.txt")


if __name__ == "__main__":
    main()