from register import register
from login import login
from projects_menu import projects_menu

def main_menu():
    while True:
        print('\n--- Welcome to Crowd Funding App ---')
        print('-------------- Main Menu -------------')
        print('1- Register')
        print('2- Login')
        print('3- Exit')
        selected = input('Choose an option: ')
        if selected == '1':
            register()
        elif selected == '2':
            user = login()
            if user:
                projects_menu(user)
        elif selected == '3':
            break
        else:
            print('Please select valid option')

if __name__ == '__main__':
    main_menu()