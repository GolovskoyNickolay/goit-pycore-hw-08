import pickle


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def list_contacts(self):
        return self.contacts


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


def main():
    book = load_data()

    while True:
        command = input("Enter command (add, remove, get, list, exit): ").strip().lower()
        if command == "add":
            name = input("Enter name: ").strip()
            address = input("Enter address: ").strip()
            book.add_contact(name, address)
        elif command == "remove":
            name = input("Enter name: ").strip()
            book.remove_contact(name)
        elif command == "get":
            name = input("Enter name: ").strip()
            print(book.get_contact(name))
        elif command == "list":
            contacts = book.list_contacts()
            for name, address in contacts.items():
                print(f"{name}: {address}")
        elif command == "exit":
            break
        else:
            print("Unknown command. Please try again.")

    save_data(book)


if __name__ == "__main__":
    main()
