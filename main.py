from library_system import Library

def menu():
    print("\n=== System Zarządzania Biblioteką ===")
    print("1. Dodaj książkę")
    print("2. Wypożycz książkę")
    print("3. Zwróć książkę")
    print("4. Pokaż dostępne książki")
    print("5. Zapisz do pliku")
    print("6. Wczytaj z pliku")
    print("0. Wyjdź")
    return input("Wybierz opcję: ")

library = Library()

while True:
    choice = menu()

    if choice == "1":
        try:
            title = input("Podaj tytuł: ")
            author = input("Podaj autora: ")
            year = int(input("Podaj rok: "))
            library.add_book(title, author, year)
        except ValueError:
            print("Rok musi być liczbą całkowitą.")
    elif choice == "2":
        title = input("Tytuł książki do wypożyczenia: ")
        library.borrow_book(title)
    elif choice == "3":
        title = input("Tytuł książki do zwrotu: ")
        library.return_book(title)
    elif choice == "4":
        library.show_available_books()
    elif choice == "5":
        filename = input("Nazwa pliku do zapisu (.csv): ")
        library.save_to_csv(filename)
    elif choice == "6":
        filename = input("Nazwa pliku do wczytania (.csv): ")
        library.load_from_csv(filename)
    elif choice == "0":
        print("Do zobaczenia!")
        break
    else:
        print("Nieprawidłowy wybór.")
