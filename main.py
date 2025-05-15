def main():
      book_path = "books/frankenstein.txt"
      current_book = get_book_text(book_path)
      print(current_book)

def get_book_text(filepath): 
        with open(filepath) as book_file:
            return(book_file.read())

main()