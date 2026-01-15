from tabulate import tabulate
from read_write_json import Projects_Data, load_json

def view_projects():
    print('\n------- Viewing All Projects --------')
    try:
        projects = load_json(Projects_Data)
        if not projects:
            print('No projects found')
            return
        print(tabulate(projects, headers='keys', stralign='center', numalign='center', tablefmt='fancy_grid'))
    except Exception as e:
        print('Something went wrong while viewing projects, Please try again')
        return