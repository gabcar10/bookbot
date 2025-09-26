#return content of the book as a string
def get_book_text(file_path):
    #open the file    
    with open(file_path) as f: # f is a file object
    #read the file
        file_contents = f.read()
    return file_contents

def word_count(full_text):
    #text is split & counted; works OK!
    word_count = len(full_text.split())
    return word_count

def main():
    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()