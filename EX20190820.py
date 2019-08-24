import xlrd
from xlutils.copy import copy
from datetime import datetime


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


def create_account():
    values = []
    limit_date = datetime(1900, 1, 1)
    limit_date2 = datetime(2002, 1, 1)
    wb = xlrd.open_workbook("test2 (another copy).xlsx")
    br = copy(wb)
    sheet1 = br.get_sheet(0)
    for sheet in wb.sheets():
        for i in range(1, sheet.nrows):
            val = sheet.cell(i, 5).value
            if val in values:
                sheet1.write(i, 7, "No")
            else:
                try:
                    bth_day = sheet.cell(i, 2).value
                    bth_day = datetime.strptime(bth_day, "%Y-%m-%d")
                except ValueError:
                    print("Data mismatch or data does not match format")
                else:
                    if limit_date < bth_day < limit_date2:
                        sheet1.write(i, 7, "Yes")
                        values.append(val)
                    else:
                        sheet1.write(i, 7, "No")

    br.save("test2 (another copy).xlsx")


create_account()

