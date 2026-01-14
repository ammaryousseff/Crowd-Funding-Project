from datetime import datetime
from read_write_json import load_json, save_json, Projects_Data

def create_project(email):
    print('------- Creating Project --------')
    while True:
        title = input('Project Title: ').strip()
        if title != '':
            break
        else:
            print('Project title cannot be empty')
    while True:
        details = input('Project Details: ')
        if details != '':
            break
        else:
            print('Project details cannot be empty')
    while True:
        target = input('Project total target "Amount in EGP": ')
        if target != '':
            break
        else:
            print('Project total target cannot be empty')
    while True:
        start = input('Start (YYYY-MM-DD): ')
        end = input('End (YYYY-MM-DD): ')
        try:
            d1 = datetime.strptime(start, "%Y-%m-%d")
            d2 = datetime.strptime(end, "%Y-%m-%d")
            if d2 > d1:
                break
            print('End date must be after start date.')
        except ValueError:
            print('Please Use format YYYY-MM-DD')
    try:
        projects = load_json(Projects_Data)
        new_project = {
            'title': title,
            'details': details,
            'target': target,
            'start_date': start,
            'end_date': end,
            'owner': email 
        }
        projects.append(new_project)
        save_json(Projects_Data, projects)
        print('\nProject Created Successfully')
    except Exception as e:
        print('Something went wrong while creating the project {e}, Please try again')