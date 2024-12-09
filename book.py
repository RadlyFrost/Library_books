import json
from typing import Optional

class Book:
    def __init__(self, title: str, author: str, year: int, book_id: Optional[int] = None, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Конвертировать объект книги в словарь для сохранения в JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """Создание объекта книги из словаря"""
        return Book(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            book_id=data['id'],
            status=data['status']
        )
