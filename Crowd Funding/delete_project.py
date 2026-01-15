from tabulate import tabulate
from read_write_json import Projects_Data, load_json, save_json

def delete_project(email):
    print('\n------- Deleting project -----------')
    projects = load_json(Projects_Data)
    my_projects = [i for i in projects if i['owner'] == email]
    if not my_projects:
        print('No projects found to delete')
        return
    # for i, d in enumerate(my_projects):
    #     print(f"{i+1}- {d['title']}")
    print(tabulate(my_projects, headers='keys', showindex=range(1, len(my_projects)+1), stralign='center', numalign='center', tablefmt='fancy_grid'))

    try:
        choice = int(input('Please select project number that you want to delete: ')) - 1
        if 0 <= choice < len(my_projects):
            selected_project = my_projects[choice]
            projects = [i for i in projects if i != selected_project]
            save_json(Projects_Data, projects)
            print('\nProject Deleted Successfully')
        else:
            print('Invalid option')
    except:
        print('Please select valid number for project, try again')
