import xlrd
from cryptography.fernet import Fernet

class User:

    def __init__(self, first_name, last_name, birthday, email, address, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.address = address
        self.username = username
        self.password = password
        self.is_logout = False

    def login(self, usr, mk):
        if self.username == usr and self.password == mk:
            print("Login Succesfully")
        else:
            print("username or password is incorrect")

    def logout(self):
        print("Are you sure to log out?")
        choose = input("Yes or No:")
        if choose == "y":
            self.is_logout = True
            print("Log Out Successfully")
        elif choose == "n":
            self.is_logout = False
            print("You still stay here")

    def update_info(self, new_first, new_last, new_birthday, new_email, new_add, new_usr, new_pasw):
        self.first_name = new_first
        self.last_name = new_last
        self.birthday = new_birthday
        self.email = new_email
        self.address = new_add
        self.username = new_usr
        self.password = new_pasw

    def print_infor(self):
        print(f"""
        first name: {self.first_name}
        last name: {self.last_name}
        birthday: {self.birthday}
        email: {self.email}
        address: {self.address}
        username: {self.username}
        password: {self.password}
        """)


A = User("Jason", "Staham", "01/01/1989", "jsonstaham@gmail.com", "USA", "jsonstaham", "123456")
A.login("jsonstaham", "123456")
A.print_infor()
A.logout()
# B = User("Vin", "Diesel", "02/02/1980", "vindiesel@gmail.com", "USA", "vindiesel", "12345")
# B.login("vindiesel", "12345")