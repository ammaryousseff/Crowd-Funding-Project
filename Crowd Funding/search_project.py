from tabulate import tabulate
from read_write_json import Projects_Data, load_json

def search_project():
    print('\n------- Search Projects -------')
    while True:
        date = input('Enter start year of projects (YYYY): ').strip()
        try:
            if date.isdigit() and len(date) == 4:
                break
        except:
            print('Please enter valid date')
    projects = load_json(Projects_Data)
    found_projects = []
    for i in projects:
        if i['start_date'].startswith(date):
            found_projects.append(i)
    if found_projects:
        print(f'Found {len(found_projects)} projects starting on {date}')
        print(tabulate(found_projects, headers='keys', stralign='center', numalign='center', tablefmt='fancy_grid'))

    else:
        print(f'No projects found starting with {date}')