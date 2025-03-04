from stats import get_file_text, get_num_words, get_character_count, sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text_location = sys.argv[1]
    book_text = get_file_text(text_location)
    # print(book_text)
    word_count = get_num_words(book_text)
    #print(f"{word_count} words found in the document")
    character_count = get_character_count(book_text)
    #print(character_count)
    sorted_count = sorted_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_location}...")
    print("----------- Word Count ----------")    
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in range(len(sorted_count)):
        if sorted_count[d]["char"].isalpha():
            print(f"{sorted_count[d]["char"]}: {sorted_count[d]["num"]}")
    print("============= END ===============")
main()