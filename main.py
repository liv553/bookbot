from stats import count_words, count_characters, sort_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print(text)
    num_words = count_words(text)
    print(f"{num_words} words found in the document\n")
    count_characters_var = count_characters(text)
    print(f"Found {num_words} total words\n")
    print(count_characters_var)
    return_list = sort_list(count_characters_var)

    for item in return_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()