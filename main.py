from stats import (
    chars_dict_to_sorted_list,
    get_num_letters,
    get_num_words,
)


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("------------ Word Count ---------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main() -> None:
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_counts = get_num_letters(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    report = print_report(book_path, num_words, sorted_chars)

    return report


if __name__ == "__main__":
    main()
