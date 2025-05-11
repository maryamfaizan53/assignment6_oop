# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_count = 0
    
    def __init__(self,book_no):
        self.book_no = book_no
        Book.display_count
    @classmethod
    def display_count(cls):
        cls.total_count += 1
        print(f"Number of books: {cls.total_count}")
        
        
        
   
        
   
        
book1 = Book(1)
book2 = Book(2)   

Book.display_count()  # Output: Number of books: 2     
        