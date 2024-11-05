# Opens book, to be handled in future functions
def open_book(title: str) -> str:
    try:
        with open(f"books/{title}.txt", "r") as book:
            return book.read()
    except FileNotFoundError as e:
        print(e)
    finally:
        book.close()


# Count words in a book
def count_words(contents: str) -> int:
    # Break book into words
    words = contents.split()
    return len(words)


# Counts the occurrence of each character in the book, counting lowercase
def count_characters(contents: str) -> dict:
    characters = {}
    for char in contents.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def main():
    frankenstein = open_book("frankenstein")
    frankenstein_word_count = count_words(frankenstein)
    print(f"There are {frankenstein_word_count} words in the book.")
    character_count = count_characters(frankenstein)
    print(character_count)


main()
