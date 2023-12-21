class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def update_author(self, new_author):
        self.author = new_author
        return f"Author updated to {new_author}"
    
    def display_book_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"

# Create instances and showcase functionality
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780141182636")
print(book1.display_book_info())
print(book1.update_author("Francis Scott Fitzgerald"))
print(book1.display_book_info())
# Create another instance
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
print(book2.display_book_info())
print(book2.update_author("Nelle Harper Lee"))
print(book2.display_book_info())
