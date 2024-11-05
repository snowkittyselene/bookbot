def open_book(title: str) -> str:
    try:
        with open(f"books/{title}.txt", "r") as book:
            return book.read()
    except FileNotFoundError as e:
        print(e)
    finally:
        book.close()


def main():
    frankenstein = open_book("frankenstein")
    print(frankenstein)


main()
