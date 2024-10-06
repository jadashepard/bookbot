def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = get_word_count(book)
    char_dict = get_char_dict(book)
    char_list = char_dict_to_sorted_list(char_dict)

    print(f"-- Begin report of {book_path} --")
    print(f"{word_count} words found in document")
    print()
    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--End report--")

def get_word_count(book):
    num_words = len(book.split())
    return num_words

def get_char_dict(book):
    char_dict = {}
    for c in book:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def char_dict_to_sorted_list(dict):
    char_list = []
    for ch in dict:
        char_list.append({"char": ch, "count": dict[ch]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

def get_book(path):
    with open(path) as f:
        return f.read()

main()
