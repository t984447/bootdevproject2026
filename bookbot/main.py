from stats import *

bookfilepath = "books/frankenstein.txt"

def main():
    ##### main
    #herpa = get_num_words(bookfilepath)

    bookText = get_book(bookfilepath)
    booksWordCounter = get_num_words(bookfilepath)

    print(f"Found {booksWordCounter} total words")

    #wordsCounted = count_letters(bookText)
    wordsCounted = count_letters_ai(bookText)
    
    print(wordsCounted)
    #for note in wordsCounted:
     #   print(f"{note}: {wordsCounted[note]}")

    print(f":: {wordsCounted["c"]}")


main()
