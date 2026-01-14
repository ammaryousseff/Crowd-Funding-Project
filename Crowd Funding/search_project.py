from datetime import datetime
from read_write_json import Projects_Data, load_json

def search_project():
    print('\n------- Search Projects -------')
    while True:
        date = input('Enter date of project to search (YYYY-MM-DD): ').strip()
        try:
            valid_date = datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print('Please enter valid date')
    projects = load_json(Projects_Data)
    found_projects = []
    for i in projects:
        if i['start_date'] == date:
            found_projects.append(i)
    if found_projects:
        print(f'Found {len(found_projects)} projects starting on {date}')
        for i, d in enumerate(found_projects):
            print(f"{i+1}- {d['title']} (Owner: {d['owner']})")
            print(f"   Target: {d['target']} EGP | Ends: {d['end_date']}")
            print('--------------------------------------------------------')
    else:
        print(f'No projects found starting with {date}')