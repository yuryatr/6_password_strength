import sys
import getpass
import string


MIN_NUMBER_CHARACTERS_PASSWORD = 5


def get_password_strength(password):
    
    password_complexity_level = 1

    if len(password) <= MIN_NUMBER_CHARACTERS_PASSWORD:
        return password_complexity_level

    if len(set(string.digits).intersection(password)):
        password_complexity_level += 3
    
    if len(set(string.ascii_lowercase).intersection(password)) \
        and len(set(string.ascii_uppercase).intersection(password)):
        password_complexity_level += 3
    
    if len(set("~`!@#$%^&*()_-+={}[]:>;',</?*-+").intersection(password)):
        password_complexity_level += 3
    
    return password_complexity_level



if __name__ == '__main__':
    try:
        usr_input_password = getpass.getpass('Password: ')
        if not usr_input_password:
            print('You did not write anything.')
            sys.exit(1)
        print('Password strength: ')
        print(get_password_strength(usr_input_password))
    except KeyboardInterrupt:
        print('Forced completion.')
    finally:
        sys.exit(0)