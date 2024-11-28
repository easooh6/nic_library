import json
class Books:
    def __init__(self,title,author,year,status):
            self.id = None
            self.title = title
            self.author = author
            self.year = year
            self.status = status

    def __str__(self):
          return "\nID: " + str(self.id) + "\nName: " + self.title + "\nAuthor: " + self.author + "\nYear: " + str(self.year) + "\nStatus:" + self.status


class Library:
        def __init__(self, filename="library_data.json"):
                self.books = self.load_books(filename) 
                self.filename = filename
                self.next_id = max([book.id for book in self.books], default=0) + 1
                
        def load_books(self, filename):
                try:
                        with open(filename, "r", encoding="utf-8") as file:
                                data = json.load(file)
                                books = [Books(book["title"], book["author"], book["year"], book["status"]) for book in data]
                                for i, book in enumerate(books):
                                        book.id = i + 1  # Assigning the ID to the books
                                return books
                except (FileNotFoundError, json.JSONDecodeError):
                        return[]
                
        def save_books(self):
                with open(self.filename, "w", encoding="utf-8") as file:
                        data = [{"title": book.title, "author": book.author, "year": book.year, "status": book.status} for book in self.books]
                        json.dump(data, file, ensure_ascii=False, indent=4)

        def add_book(self, title, author, year):
                new_book = Books(title,author,year,"Available")
                new_book.id = self.next_id
                self.next_id += 1
                self.books.append(new_book)
                self.save_books()
                print("The book was added", new_book)

        def search_book(self, search_term):
                found_books = []
                for book in self.books:
                        if (search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term.lower() in str(book.year)):
                                found_books.append(book)
                if (found_books):
                        print("Found books: ")
                        for book in found_books:
                                print(book)
                else:
                        print("No book found.")
        
        def update_status(self, book_id, new_status):
                for book in self.books:
                        if (book.id == book_id):
                                book.status = new_status
                                self.save_books()
                                print("Status of book " + '"' + book.title + '"'  + " was changed to " + book.status)
                                return
                else:
                        print("Book not found")

        def remove_book(self,book_id):
                for book in self.books:
                        if book.id == book_id:
                                self.books.remove(book)
                                self.save_books()
                                print("The book " + '"' + book.title + '"' + " was removed")
                                return
                else:
                        print("Book not found")

        def show_books(self):
                if (self.books):
                        print("The books in the library:")
                        for book in self.books:
                                print(book)
                else:
                        print("No books in the library")
library = Library()

def main_menu():
        while True:
                print("welcome to the library app. Choose the option you want to use:")
                print("1. Add the book")
                print("2. Search the book")
                print("3. Update the status of the book")
                print("4. Remove the book")
                print("5. Show all books")
                print("6. Exit")
                choice = int(input())
                if (choice == 1):
                        title = input("Enter the title of the book:\n")
                        author = input("Enter the author of the book:\n")
                        try:
                                year = int(input("Enter the year of the book\n"))
                                library.add_book(title,author,year)
                        except ValueError:
                                print("Invalid year. Enter a number\n")
                elif (choice == 2):
                        search_term = input("Enter the title of the book, the year it was published or the author\n")
                        library.search_book(search_term)
                elif (choice == 3):
                        try:
                                book_id = int(input("Enter the id of the book\n"))
                                while True:
                                        new_status = input("Enter a new status of the book(available/not available)\n")
                                        new_status.lower()
                                        if (new_status in ["available", "not available"]):  
                                                break
                                        else:
                                                print("Invalid status. Please enter: available/not available\n")
                                library.update_status(book_id, new_status)
                        except ValueError:
                                print("Invalid ID. Enter an integer value\n")
                elif (choice == 4):
                        try:
                                book_id = int(input("Enter the id of the book\n"))
                                library.remove_book(book_id)
                        except ValueError:
                                print("Invalid ID. Enter an integer value\n")
                elif (choice == 5):
                        library.show_books()
                elif (choice == 6):
                        print("Thank you for using my app!\n")
                        break
                else:
                        "Invalid choice. Please try again\n"

main_menu()
