from stats import get_book_text
from stats import word_count
from stats import repeat_chars
from stats import sorted_dict
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    

    path_to_file = sys.argv[1]
    returned_contents = get_book_text(path_to_file)
    num_words = word_count(returned_contents)
    num_chars = repeat_chars(returned_contents)
    sorted_chars = sorted_dict(num_chars)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()