import sys
import stats

def get_book_text(filepath):
    #  It takes a filepath as input and returns the contents of the file as a string.
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    text = get_book_text(book_filepath)
    
    print(f"----------- Word Count ----------")
    num_words = stats.get_num_words(text)
    print(f"Found {num_words} total words")

    print(f"--------- Character Count -------")
    characters = stats.get_num_characters(text)
    sorted = stats.get_sorted_list(characters)
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()