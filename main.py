def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    print_report(book,book_path)

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

def print_report(book,path):
    word_count = get_word_count(book)
    char_dict = get_char_dict(book)
    char_list = []
    for char,count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)

    print(f"-- Begin report of {path} --")
    print(f"{word_count} words found in document\n")
    for item in char_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--End report--")

def sort_on(dict):
    return dict["count"]

def get_book(path):
    with open(path) as f:
        return f.read()

main()
