from stats import word_count
from stats import char_count
from stats import sort_by_count
import sys

#return content of the book as a string
def get_book_text(file_path):
    #open the file    
    with open(file_path) as f: # f is a file object
    #read the file
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book> (books/Title)")
        sys.exit(1)

    print("============ BOOKBOT ============")
    #book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}")
    #word counter
    num_words = word_count(get_book_text(book_path))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #character counter (dictionary of occurrence)
    dict_char = {}
    unsorted_dict = {}
    dict_char = char_count(get_book_text(book_path))
    for char in dict_char:
        count = dict_char[char]
        unsorted_dict.update({char: count})
        #print(f"character: {char}, occurrences: {count}; ")        #neater presentation
        #print(f"'{char}': {count}")                                 #simpler, as required for the exercise
    sorted_list = sort_by_count(unsorted_dict)
    #print(sorted_list)
    
    print("----------- Character Count ----------")
    for dico in sorted_list:
        #discard non alphanumerical characters        
        if dico["char"].isalpha():
            print(f"{dico['char']}: {dico['num']}")

main()

'''NICE TO DO: How would I go about ordering (ASC or DESC) the result?
as it stands, the characters are ordered on the base of which appears first in the document.
I'd have to compare (loop on) the dictionary against a pre-ordered list and complete a new ordered dictionary.'''