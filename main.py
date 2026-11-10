from menu import show_menu
from data import books
from logic import (display_books,
                   search_book,
                   add_book,
                   borrow_book,
                   return_book,
                   get_available_books,
                   get_books_by_author
                   )



def main():
    user_choice = ""
    
    while user_choice != "8":
        show_menu()
    
        user_choice = input("Choose an option: ")
        print()
        
        if user_choice == "1":
            display_books(books)
        
        elif user_choice == "2":
            name = input("Enter book name: ")
            print(search_book(books, name))
            
        elif user_choice == "3":
            book_name = None
            author_name = None
            
            while not book_name:
                book_name = input("Enter book name: ").strip()
                if not book_name:
                    print("\nChoice cannot be empty!")
                    print("Try again\n")
        
            while not author_name:
                author_name = input("Enter author name: ").strip()
                if not author_name:
                    print("\nChoice cannot be empty!")
                    print("Try again\n")
        
            integer_year = False
            while not integer_year:
                try:
                    publication_year = int(input("Enter year of publication: "))
                    if publication_year > 0:
                        integer_year = True
                    else:
                        print()
                        print("Publication year must be positive\n")
                except ValueError:
                    print()
                    print("Publication year must be numbers\n")
                    integer_year = False
                            
            add_book(books, book_name, author_name, publication_year)
            
        elif user_choice == "4":
            book_id = int(input("Enter book ID: "))
            
            borrow_book(books, book_id)
            
        elif user_choice == "5":
            book_id = int(input("Enter book ID: "))
            
            return_book(books, book_id)
            
        elif user_choice == "6":
            print(get_available_books(books))
            
        elif user_choice == "7":
            author = input("Enter author name: ")
            
            print(get_books_by_author(books, author))
        
        elif user_choice != "8":
            print("Invalid choice\nChoice must be 1-8")
            
        
        
            
if __name__ == "__main__":
    main()