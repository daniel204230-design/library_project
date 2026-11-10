
def display_books(books):
    for book in books:
        print(book)
    
    
def search_book(books, name):
    related_books = []
    
    for book in books:
        if name.lower() in book.get("name").lower():
            related_books.append(book)
            
    if not related_books:
        return None
            
    return related_books
        
        
def add_book(books, name, author, year):
    for book in books:
        if name == book["name"] and author == book["author"]:
            print("Book alredy exist")
            return False
        books.append(
            {
            "id": get_next_book_id(books),
            "name":name,
            "author":author,
            "year": year,
            "available": True
            }
            )
        print("\nThe book added successfully")
        return True
        
        
def borrow_book(books, book_id):
    for book in books:
        if book_id == book["id"]:
            if book["available"] == True:
                book["available"] = False
                print(f"{book["name"]} was successfully borrowed.")
                print("Happy reading")
                return True
            print("The requested book is not available for borrow")
            return False
    print("Book does not exist")
    return False


def return_book(books, book_id):
    for book in books:
        if book_id == book["id"]:
            if book["available"] == False:
                book["available"] = True
                print(f"{book["name"]} was successfully returned.")
                return True
            print("The book is already in stock")
            return False
    print("Book does not exist")
    return False


def get_available_books(books):
    available_books = []
    
    for book in books:
        if book["available"] == True:
            available_books.append(book["name"])
    return available_books


def get_books_by_author(books, author):
    books_by_author = []
    
    for book in books:
        if author == book["author"]:
            books_by_author.append(book["name"])
    return books_by_author


def get_next_book_id(books):
    new_id = books[-1]["id"] + 1
    return new_id
    
    




