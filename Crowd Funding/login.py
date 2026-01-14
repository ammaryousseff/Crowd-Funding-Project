import pwinput
from read_write_json import Users_Data, load_json

def login():
    print('Please fill next to Login')
    try:
        login_email = input('Enter your email: ').strip()
        login_password = pwinput.pwinput('Enetr your password: ')
        users = load_json(Users_Data)
        for user in users:   
            if user['email'] == login_email and user['password'] == login_password:
                    print(f'\nLogin Successful, Welcome {user['first_name']}')
                    return login_email
        print('Wrong email or password, please try again')
        return False
    except Exception as e:
        print(f'Error happened during login {e}')
        return False