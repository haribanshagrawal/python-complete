#Aggregation -> represents a relationship where one object (the whole) contains refreences to one or more independent objects (the parts)

#in the below example Library and Book class can exist independently. 
#also Library has aggregation of Books class

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        
    def add_book(self,book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
library=Library("Central Library")
book1 =Book("My Life and Work","Henry Ford")
book2=Book("Sialkot Saga","Ashwin Sanghi")
book3=Book("Wings of Fire","A. P. J Abdul Kalam")

for book in [book1,book2,book3]:
    library.add_book(book)
    
print(library.name)
for book in library.list_books():
    print(book)
    