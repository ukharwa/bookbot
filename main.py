def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    print("--REPORT ON " + book_path + "--")
    print("This book contains " + str(words) + " words")
    characters = character_count(text)
    sortedDict = sorted(characters.items(), key=lambda x:x[1], reverse=True)
    print(sortedDict)
    for key in sortedDict:
        print("The character \"" + key[0] +"\" appeared " + str(key[1]) + " times")

    print("--END OF REPORT--")        

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for c in text:
        lower = c.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1        
    return characters

main()
