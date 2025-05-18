from stats import count_words, count_chars, letter_sort
import sys

if len(sys.argv) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

def main():
    book_path = sys.argv[1]
    current_book = get_book_text(book_path)
    num_words = count_words(current_book)
    chars_dict = count_chars(current_book)
    chars_sorted_list = letter_sort(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(filepath): 
        with open(filepath) as book_file:
            return(book_file.read())


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in chars_sorted_list:
        print(i['char'],": ", i['num'], sep='')

    print("============= END ===============")


main()