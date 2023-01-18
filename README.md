CSEC 507 - APPLIED CRYPTOLOGY
============================
Homework 1
----------
### Encoding and Decoding Caesar Ciphers

-In order to encode or decode Caesar Cipher, functions inside the caesarCipher.py file can be utilized by modifying and calling necessary functions inside the main function and running the file by executing
`python3 caesarCipher.py` command.

-For encoding, the encodeCaesarCipher function can be called with the following parameters:
`encodeCaesarCipher(plaintext, key)`
where plaintext is the string to be encoded and key is the shift value.

-For decoding, the decodeCaesarCipher function can be called with the following parameters:
`decodeCaesarCipher(ciphertext, key)`
where ciphertext is the string to be decoded and key is the shift value.

`tryDecode(cipherText)` function can be called to try decoding the cipherText with observing all possible shift values.

### Frequency Analysis

* In order to perform frequency analysis, functions inside the frequencyAnalysis.py file can be utilized by modifying and calling necessary functions inside the main function and running the file by executing
`python3 frequencyAnalysis.py` command.

* For performing frequency analysis on the file, the getStatistics function can be called with the following parameters:
`getStatistics(filename)`
where filename is the string, the name of the file to be analyzed.

* For getting ngrams from the file, the getNgrams function can be called with the following parameters:
`getNgrams(filename, n)`
where filename is the string, the name of the file to be analyzed and n is the integer, the length of the ngrams.

* For getting doubled letters from the file and their occurrences, getDoubles function can be called with the following parameters:
`getDoubles(filename)`
where filename is the string, the name of the file to be analyzed.

With the help of those statistical information, the file can be analyzed and the most probable plaintext can be found.
In order to perform replace operations on the file with ciphertext letters and corresponding alphabet letters,
a Text class is defined inside the replaceLetter.py file. 

* The class can be instantiated with the following parameters:
`text = Text(textString)`
where textString is the string, the text to be analyzed, after reading the file and getting the textString by using readFile(filename) function,
where filename is the string, the name of the file to be analyzed.
* A replace method defined for the Text class can be called with the following parameters:
`text.replace(cipherLetter, alphabetLetter)`
where cipherLetter is the string, the letter to be replaced and alphabetLetter is the string, the letter to be replaced with. It is also recommended that
while calling the replace method, do not use lowercase letters if ciphertext is lowercase and uppercase letters if ciphertext is uppercase; in order to avoid inconsistencies.
* `decryptTurkishCipher()` and `decryptEnglishCipher()` functions can be called to decrypt the ciphertexts seperately, by calling Text.replace method manually. These functions are just for nothing but avoiding inconvenience.
* With calling the necessary functions, the file can be decrypted and the most probable plaintext can be found step by step analyzing the frequencies manually.
Replacement can be observed by running the file by executing `python3 replaceLetter.py` command.