from stats import *
import sys

if (len(sys.argv)) >= 2:
    bookfilepath = sys.argv[1]
elif (len(sys.argv)) <= 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    ##### main
    ## Get book
    bookText = get_book(bookfilepath)
    ## Count words
    booksWordCounter = get_num_words(bookfilepath)

    ## mandatory print words


    ## Get letter and their count
    wordsCounted = count_letters(bookText)
    
    ## Sord the letters by their count
    wordCountSorted = chars_dict_to_sorted_list(wordsCounted)
    #print(wordCountSorted)

    print_report(bookfilepath, booksWordCounter, wordCountSorted)


main()
