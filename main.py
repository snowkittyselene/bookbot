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


# Sorts the character frequency and returns only alphabetic chars
def filter_characters(frequencies: dict) -> dict:
    letters_only = {}
    for char in frequencies:
        if char.isalpha():
            letters_only[char] = frequencies[char]
    return dict(
        sorted(letters_only.items(), key=lambda letter: letter[1], reverse=True)
    )


# Creates and prints report of the book
def create_report(title: str) -> None:
    # Open book first, then get stats
    book = open_book(title)
    word_count = count_words(book)
    character_count = count_characters(book)
    sorted_characters = filter_characters(character_count)

    # Assemble report
    print(f"--- Begin report of {title.title()} ---")
    print("")
    print(f"There were {word_count} words found in the document.")
    for character in sorted_characters:
        print(
            f"The {character} character was found {sorted_characters[character]} times"
        )
    print("")
    print("--- End report ---")


def main():
    create_report("frankenstein")


main()
