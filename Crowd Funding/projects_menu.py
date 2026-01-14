from create_project import create_project
from view_projects import view_projects
from edit_project import edit_project
from delete_project import delete_project
from search_project import search_project

def projects_menu(email):
    while True:
        print('\n----- Projects Dashboard -----')
        print('1- Create project')
        print('2- View all projects')
        print('3- Edit my projects')
        print('4- Delete my project')
        print('5- Search for a project by date')
        print('6- Logout')

        choice = input('\nChoose an option: ')

        if choice == '1': 
            create_project(email)
        elif choice == '2': 
            view_projects()
        elif choice == '3': 
            edit_project(email)
        elif choice == '4': 
            delete_project(email)
        elif choice == '5': 
            search_project()
        elif choice == '6': 
            print("Logging out")
            break
        else: 
            print('Please select valid option')