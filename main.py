#return content of the book as a string
def get_book_text(file_path):
    #open the file    
    with open(file_path) as f: # f is a file object
    #read the file
        file_contents = f.read()

    return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()