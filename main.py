from stats import words_counter, characters_counter
from stats import create_char_num_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # book_text = get_book_text("books/frankenstein.txt")
    book_text = get_book_text(sys.argv[1])
    num_words = words_counter(book_text)
    # print(f"Found {num_words} total words")

    num_chars = characters_counter(book_text)
    # print(num_chars)

    char_num_dictionary = create_char_num_dictionary(num_chars)
    # print(char_num_dictionary)

    print("============ BOOKBOT ============")
    # print("Analyzing book found at books/frankenstein.txt...")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_num_dictionary:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()