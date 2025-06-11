import csv

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": str(self.available)
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], int(data['year']), data['available'] == 'True')

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))
        print("Dodano książkę!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print("Wypożyczono książkę!")
                return
        print("Książka niedostępna lub nie istnieje.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print("Zwrócono książkę!")
                return
        print("Nie znaleziono wypożyczonej książki o tym tytule.")

    def show_available_books(self):
        available = list(filter(lambda b: b.available, self.books))
        if not available:
            print("Brak dostępnych książek.")
        else:
            for book in available:
                print(f"{book.title} – {book.author} ({book.year})")

    def save_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["title", "author", "year", "available"])
                writer.writeheader()
                for book in self.books:
                    writer.writerow(book.to_dict())
            print("Dane zapisane do pliku.")
        except Exception as e:
            print(f"Błąd zapisu: {e}")

    def load_from_csv(self, filename):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.books = list(map(Book.from_dict, reader))
            print("Dane wczytane z pliku.")
        except FileNotFoundError:
            print("Plik nie istnieje.")
        except Exception as e:
            print(f"Błąd odczytu: {e}")
