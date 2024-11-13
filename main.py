def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = countWords(file_contents)
        charsCount = characterCount(file_contents)
        print(words)
        print(charsCount)
        printReport(charsCount)

def countWords(text):
    return len(text.split())

def characterCount(text):
    loweredText = text.lower()
    characters = {}
    for c in loweredText:
        if c in characters:
            characters[c] = characters[c] +1
        else:
            characters[c] = 1
    #print(characters)
    return characters

def sort_on(dict):
    return dict["times"]

def printReport(dict):
    charList = []
    for c in dict:
        if c.isalpha():
            #print(f'{c} is repeated {dict[c]} times')
            charList.append({"letter": c, "times": dict[c]})
    charList.sort(reverse=True, key=sort_on)
    for c in charList:
        print(f'The {c["letter"]} character was found {c["times"]} times')


main()