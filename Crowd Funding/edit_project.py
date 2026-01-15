from tabulate import tabulate
from datetime import datetime
from read_write_json import Projects_Data, load_json, save_json

def edit_project(email):
    print('\n------ Editing my projects -------')
    projects = load_json(Projects_Data)
    my_projects = [i for i in projects if i['owner'] == email]
    if not my_projects:
        print('No project found associated with your email')
        return
    # for i, d in enumerate(my_projects):
    #     print(f"{i+1}- {d['title']}")
    print(tabulate(my_projects, headers='keys', showindex=range(1, len(my_projects)+1), stralign='center', numalign='center', tablefmt='fancy_grid'))

    try:
        choice = int(input('Please select project number that you want to edit: ')) - 1
        if 0 <= choice < len(my_projects):
            selected_project = my_projects[choice]
            for i in projects:
                if i == selected_project:
                    current_project = i
                    break
            while True:
                print(f"\n--- Editing: {current_project['title']} ---")
                print(f"1- Title    (Current: {current_project['title']})")
                print(f"2- Details  (Current: {current_project['details']})")
                print(f"3- Target   (Current: {current_project['target']})")
                print(f"4- Dates    (Current: {current_project['start_date']} -> {current_project['end_date']})")
                print('5- Go Back')
                edit_choice = input('Select the field that you want to edit: ')
                if edit_choice == '1':
                    new_title = input('Enter new title: ').strip()
                    if new_title: 
                        current_project['title'] = new_title
                        print('\nTitle Updated')
                elif edit_choice == '2':
                    new_details = input('Enter new details: ').strip()
                    if new_details:
                        current_project['details'] = new_details
                        print('Details Updated')
                elif edit_choice == '3':
                    new_target = input('Enetr new target: ').strip()
                    if new_target.isdigit():
                        current_project['target'] = new_target
                        print('Target Updated')
                    else:
                        print('Please enter valid number')
                elif edit_choice == '4':
                    while True:
                        try:
                            new_start = input('New start (YYYY-MM-DD): ').strip()
                            new_end = input('New end (YYYY-MM-DD): ').strip()
                            start = new_start if new_start else current_project['start_date']
                            end = new_end if new_end else current_project['end_date']
                            d1 = datetime.strptime(start, "%Y-%m-%d")
                            d2 = datetime.strptime(end, "%Y-%m-%d")
                            if d2 > d1:
                                current_project['start_date'] = start
                                current_project['end_date'] = end
                                print('Date Updated')
                                break
                            print("End date must be after start date")
                        except:
                            print('Please use valid format YYYY-MM-DD')
                elif edit_choice == '5':
                    save_json(Projects_Data, projects)
                    print('\nAll changes saved\n')
                    break
                else:
                    print('Invalid option')
        else:
            print('Invalid option') 
    except Exception as e:
        print(f'Something went wrong {e}, please try again')