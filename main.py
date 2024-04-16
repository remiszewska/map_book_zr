from models.data_source import users
from utils.crud import read_friends


if __name__ == '__main__':
    while True:
        print("Welcome to the menu choose an option: ")
        print("0. Exit")
        print("1. Read a list of friends")
        menu_option = input("Choose an option: ")
        if menu_option == "0":
            break
        if menu_option == "1":
            read_friends(users)


