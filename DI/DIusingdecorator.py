from typing import Callable, Dict, List
from dataclasses import dataclass
import functools

# --- DI Container with Decorators ---
class DIContainer:
    _services: Dict[str, Callable] = {}

    @classmethod
    def register(cls, name: str):
        def decorator(factory: Callable):
            cls._services[name] = factory
            print(f"Registered '{name}'")
            return factory
        return decorator

    @classmethod
    def resolve(cls, name: str):
        if name not in cls._services:
            raise Exception(f"Service '{name}' not found")
        print(f"Resolving '{name}'")
        return cls._services[name]()

# --- Interfaces ---
class IDataBaseConnection:
    def connect(self): pass
    def query(self, sql: str) -> List[Dict]: pass

class IBookRepository:
    def find_all_books(self) -> List[Dict]: pass
    def save_book(self, book: Dict): pass

# --- Implementations ---
@dataclass
class MongoDBConnection(IDataBaseConnection):
    connection_string: str

    def connect(self):
        print("MongoDB Connection established")

    def query(self, sql: str) -> List[Dict]:
        print("MongoDB Query:", sql)
        return [
            {"id": 1, "title": "Clean Code", "author": "Robert Martin"},
            {"id": 2, "title": "Design Patterns", "author": "Gang of Four"}
        ]

@dataclass
class BookRepository(IBookRepository):
    database: IDataBaseConnection

    def find_all_books(self) -> List[Dict]:
        self.database.connect()
        return self.database.query("SELECT * FROM books")

    def save_book(self, book: Dict):
        self.database.connect()
        print("Saving Book:", book["title"])

@dataclass
class BooksService:
    repository: IBookRepository

    def get_all_books(self) -> List[Dict]:
        print("Fetching all books through service...")
        return self.repository.find_all_books()

    def add_book(self, title: str, author: str):
        book = {"title": title, "author": author, "id": "some-id"}
        print("Adding book through service...")
        self.repository.save_book(book)

# --- DI Registration with Decorators ---
@DIContainer.register("database")
def get_database():
    return MongoDBConnection("mongodb://localhost:27017/bookstore")

@DIContainer.register("repository")
def get_repository():
    db = DIContainer.resolve("database")
    return BookRepository(db)

@DIContainer.register("bookService")
def get_book_service():
    repo = DIContainer.resolve("repository")
    return BooksService(repo)

# --- Execution ---
book_service = DIContainer.resolve("bookService")
print("------------------------")
book_service.add_book("NestJS Mastery", "John")
books = book_service.get_all_books()
print("Retrieved books:", books)