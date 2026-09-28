# 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hi,My name is {self.name} and I am {self.age} years old.")


student1 = Student("Sukanta", 21)
print(student1.name)
student1.introduction()


# 2
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance


my_account = BankAccount("Sam")
print(my_account.deposit(100))
print(my_account.withdraw(150))

# 3


class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow(self,book_object):
        book_object.is_checked_out = True
        self.borrowed_books.append(book_object)
        print(f"{self.name} just borrowed {book_object.title}!")
        
book1 = Book("1984", "George Orwell")
reader1 = Reader("Charlie")

reader1.borrow(book1)
