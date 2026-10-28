DELIMITER = ","

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

def collectWords():
    words = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if words == "":
            words = word
        else:
            words += DELIMITER + word
    return words

def analyseWords(Pwords):
    if Pwords == "":
        wordList = []
    else:
        wordList = Pwords.split(DELIMITER)

    wordCounter = len(wordList)
    charCounter = sum(len(word) for word in wordList)

    if wordCounter > 0:
        average = charCounter / wordCounter
    else:
        average = 0

    print(f"- {wordCounter} Words")
    print(f"- {charCounter} Characters")
    print(f"- {average:.2f} Average word length")

main()

