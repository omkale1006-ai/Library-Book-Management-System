# -------------------------------
# 📚 Library Book Management System
# -------------------------------

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("📭 No books in the library.")
            return

        print("\n📖 Library Book List:")
        for book in self.books:
            print(f"🔹 {book.book_id} | {book.title} by {book.author} | Copies: {book.copies}")

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"✅ Found: {book.title} by {book.author} | Copies: {book.copies}")
                found = True
                break
        if not found:
            print("❌ Book not found.")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.copies > 0:
                    book.copies -= 1
                    print(f"📗 You borrowed: {book.title}")
                else:
                    print("⚠️ Book is currently not available.")
                return
        print("❌ Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.copies += 1
                print(f"📘 You returned: {book.title}")
                return
        print("❌ Book ID not found.")


def main():
    library = Library()

    while True:
        print("\n====== 📚 Library Menu ======")
        print("1️⃣  Add Book")
        print("2️⃣  Show All Books")
        print("3️⃣  Search Book by Title")
        print("4️⃣  Borrow Book")
        print("5️⃣  Return Book")
        print("6️⃣  Exit")
        print("=============================")

        choice = input("👉 Enter your choice (1-6): ")

        if choice == '1':
            book_id = input("📌 Enter Book ID: ")
            title = input("📖 Enter Book Title: ")
            author = input("✍️  Enter Author Name: ")
            try:
                copies = int(input("📦 Enter Number of Copies: "))
                library.add_book(Book(book_id, title, author, copies))
            except ValueError:
                print("⚠️ Invalid number of copies.")

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("🔍 Enter Book Title to Search: ")
            library.search_book(title)

        elif choice == '4':
            book_id = input("📕 Enter Book ID to Borrow: ")
            library.borrow_book(book_id)

        elif choice == '5':
            book_id = input("📘 Enter Book ID to Return: ")
            library.return_book(book_id)

        elif choice == '6':
            print("👋 Exiting Library System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 to 6.")

# Run the program
main()
