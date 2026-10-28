DELIMITER = ","

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

def collectWords():
    words = ""
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        else:
            if words == "":
                words = word
            else:
                words += DELIMITER + word
    return words

def analyseWords(Pwords):
    wordList = Pwords.split(DELIMITER)
    wordCounter = 0
    charCounter = 0
    for word in wordList:
        wordCounter += 1
        charCounter += len(word)
    if Pwords == "":
        wordCounter = 0
    print(f"- {wordCounter} words")
    print(f"- {charCounter} Characters")
    if wordCounter > 0:
        average = charCounter / wordCounter
    else:
        average = 0
    print("- {:.2f} Average word length".format(average))
    
main()

