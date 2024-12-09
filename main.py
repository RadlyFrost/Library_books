import sys
from library import Library

def show_books(library):
    books = library.list_books()
    print("\nСписок книг:")
    if books:
        for book in books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
    else:
        print("Нет книг в библиотеке.")

def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите опцию: ").strip()

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
            print("Книга добавлена!")

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            if library.remove_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга с таким ID не найдена.")

        elif choice == '3':
            search_term = input("Введите данные для поиска (название, автор или год): ")
            books = library.find_books(search_term)
            show_books(library)
        
        elif choice == '4':
            show_books(library)

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            if library.change_status(book_id, new_status):
                print("Статус изменен.")
            else:
                print("Не удалось изменить статус.")

        elif choice == '6':
            print("Выход из программы.")
            sys.exit()

        else:
            print("Неверная опция, попробуйте снова.")

if __name__ == "__main__":
    main()
