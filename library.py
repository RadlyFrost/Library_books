import json
from typing import List, Optional
from book import Book

class Library:
    def __init__(self, data_file: str = 'data.json'):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает книги из файла"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        """Сохраняет список книг в файл"""
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку"""
        book_id = max([book.id for book in self.books], default=0) + 1
        book = Book(title, author, year, book_id)
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу по id"""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_books(self, search_term: str) -> List[Book]:
        """Ищет книги по title, author или year"""
        return [book for book in self.books if (
            search_term.lower() in book.title.lower() or
            search_term.lower() in book.author.lower() or
            search_term == str(book.year)
        )]

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """Находит книгу по id"""
        return next((book for book in self.books if book.id == book_id), None)

    def change_status(self, book_id: int, new_status: str) -> bool:
        """Меняет статус книги"""
        book = self.find_book_by_id(book_id)
        if book and new_status in ["в наличии", "выдана"]:
            book.status = new_status
            self.save_books()
            return True
        return False

    def list_books(self) -> List[Book]:
        """Возвращает все книги библиотеки"""
        return self.books
