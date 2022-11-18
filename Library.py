class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t*" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            date = input("Enter present date: ")
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            with open("LibraryRecord.txt", "a") as f:
                f.write(f"{Name}\t{bookName}\t{date} has borrowed this book.\n")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry, This {bookName} book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        date = input("Enter present date: ")
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        with open("LibraryRecord.txt", "a") as f:
                f.write(f"{Name}\t{bookName}\t{date} had returned this book.\n")

class Student:
    def requestBook(self):
        borrbook = input("Enter the name of the book you want to borrow: ")
        return borrbook

    def returnBook(self):
        retbook = input("Enter the name of the book you want to return: ")
        return retbook

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    Name = input("Enter your name: ")
    print(f"Hello {Name},")
    a = 0
    while(a == 0):
        welcomeMsg = ''' ====== Welcome to Central Library ======\n'''
        print(welcomeMsg)
        a += 1
        while(True):
            Navigation ='''Please choose an option:
            1. List all the books.
            2. Request a book.
            3. Add/Return a book.
            4. Exit the library.
            '''
            print(Navigation)
            try:
                 a = int(input("Enter an option from above: "))
            except ValueError as e:
                print("Invalid Input")
            if a == 1:
                centralLibrary.displayAvailableBooks()
            elif a == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for choosing Central Library. Have a great day ahead!")
                exit()
            else:
                print("Invalid Choice!")