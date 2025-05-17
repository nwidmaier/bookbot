def main():
      book_path = "books/frankenstein.txt"
      current_book = get_book_text(book_path)
      print(count_words(current_book))

def get_book_text(filepath): 
        with open(filepath) as book_file:
            return(book_file.read())
        
def count_words(current_book):
    raw_words = current_book.split()
    word_count= 0

    for i in raw_words:
        word_count += 1
    return(word_count)    
      

main()