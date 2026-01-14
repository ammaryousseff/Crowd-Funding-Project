import re
import pwinput
from read_write_json import Users_Data, save_json, load_json

def register():
    print('Please fill next to Register')
    users = load_json(Users_Data)
    try:
        while True:
            fname = input('Enter your first name: ').strip()
            if fname != '' and fname.isalpha():
                break
            else:
                print('Name cannot be empty')
        while True:
            lname = input('Enter your last name: ').strip()
            if lname != '' and fname.isalpha():
                break
            else:
                print('Name cannot be empty')
        while True:
            email = input('Please enter your email: ').strip()
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.fullmatch(pattern, email):
                email_exist = False
                for user in users:
                    if user['email'] == email:
                        email_exist = True
                        print(f'The email {email} is already registered, please try another one')
                        break
                if email_exist:
                    continue
                break
            else:
                    print('Please enter correct email')
        while True:
            password = pwinput.pwinput(prompt='Enter password: ')
            confirm_password = pwinput.pwinput(prompt='Confirm password: ')
            if password == confirm_password and password != '':
                break
            else:
                print('Password not match, please enter it again')
        while True:
            phone = input('Enter your phone number: ').strip()
            if phone.isdigit() and len(phone) == 11 and phone.startswith(('010', '011', '012', '015')):
                break
            else:
                print('Please enter correct egyptian phone number')
        
        new_user = {
            "first_name": fname,
            "last_name": lname,
            "email": email,
            "password": password,
            "phone": phone
        }
        users.append(new_user)
        save_json(Users_Data, users)
        print('\nRegistration Completed Successfully, You can login now')
    except Exception as e:
        print(f'Error happened during registeration {e}')