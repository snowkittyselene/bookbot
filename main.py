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


def main():
    frankenstein = open_book("frankenstein")
    frankenstein_word_count = count_words(frankenstein)
    print(f"There are {frankenstein_word_count} words in the book.")


main()
