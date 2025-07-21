from typing import List, Dict, Callable

# --- Interfaces ---
class IDataBaseConnection:
    def connect(self) -> None:
        pass

    def query(self, sql: str) -> List[Dict]:
        pass


class IBookRepository:
    def find_all_books(self) -> List[Dict]:
        pass

    def save_book(self, book: Dict) -> None:
        pass

# --- Concrete Database Implementations ---
class MongoDBConnection(IDataBaseConnection):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connect(self) -> None:
        print("MongoDB Connection established")

    def query(self, sql: str) -> List[Dict]:
        print("MongoDB Query:", sql)
        return [
            {"id": 1, "title": "Clean Code", "author": "Robert Martin"},
            {"id": 2, "title": "Design Patterns", "author": "Gang of Four"}
        ]

# Add other DB classes here (PostgreSQLConnection, MySQLConnection) similarly if needed

# --- Repository ---
class BookRepository(IBookRepository):
    def __init__(self, database: IDataBaseConnection):
        print("BookRepository initialized with injected database")
        self.database = database

    def find_all_books(self) -> List[Dict]:
        self.database.connect()
        return self.database.query("SELECT * FROM books")

    def save_book(self, book: Dict) -> None:
        self.database.connect()
        print("Saving Book:", book["title"])

# --- Service ---
class BooksService:
    def __init__(self, repository: BookRepository):
        print("BookService initialized with injected repository")
        self.repository = repository

    def get_all_books(self) -> List[Dict]:
        print("Fetching all books through service...")
        return self.repository.find_all_books()

    def add_book(self, title: str, author: str) -> None:
        book = {"title": title, "author": author, "id": "some-id"}  # You can use uuid
        print("Adding book through service...")
        self.repository.save_book(book)

# --- DI Container ---
class DIContainer:
    def __init__(self):
        self.services: Dict[str, Callable] = {}

    def register(self, name: str, factory: Callable) -> None:
        self.services[name] = factory
        print(f"Registered service '{name}'")

    def resolve(self, name: str):
        if name not in self.services:
            raise Exception(f"Service '{name}' not found")
        print(f"Resolving service '{name}'")
        return self.services[name]()

# --- Setup and Execution ---
container = DIContainer()
container.register("database", lambda: MongoDBConnection("mongodb://localhost:27017/bookstore"))
container.register("repository", lambda: BookRepository(container.resolve("database")))
container.register("bookService", lambda: BooksService(container.resolve("repository")))

book_service: BooksService = container.resolve("bookService")
print("----------------------")
book_service.add_book("NestJS Mastery", "John")
books = book_service.get_all_books()
print("Retrieved books:", books)

