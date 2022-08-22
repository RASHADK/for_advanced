class library:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.books = []

    def book_taken(self,book):
        self.books.append(book)

    def book_returned(self,book):
        self.books.remove(book)

    def display(self):
        print(self.name, self.address, self.phone_number)
        print("Books:")
        print(self.books)


obj = library("Nikhil", "karnataka", "12345")
obj.book_taken("python")
obj.book_taken("java")
obj.book_taken("c++")
obj.display()
obj.book_returned("python")
obj.display()
obj.book_taken("c")
obj.display()
obj.book_returned("c")
obj.display()