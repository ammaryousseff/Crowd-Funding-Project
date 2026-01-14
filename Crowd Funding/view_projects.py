from read_write_json import Projects_Data, load_json

def view_projects():
    print('\n------- Viewing All Projects --------')
    try:
        projects = load_json(Projects_Data)
        if not projects:
            print('No projects found')
            return
        for i, d in enumerate(projects):
            print(f'{i+1}- {d['title']} (Owner: {d['owner']})')
            print(f'   Target: {d['target']} EGP | {d['start_date']} -> {d['end_date']}')
            print('-------------------------------------------------------------')
    except Exception as e:
        print('Something went wrong while viewing projects, Please try again')
        return