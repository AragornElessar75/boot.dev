
def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_num_letters(text: str) -> dict[str, int]:
    letter_count: dict[str, int] = {}
    for char in text.lower():
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def sort_on(letter: tuple[str, int]) -> int:
    return letter[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    char_list = list(char_counts.items())
    return sorted(char_list, key=sort_on, reverse=True)
