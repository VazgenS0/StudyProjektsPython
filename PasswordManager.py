from cryptography.fernet import Fernet
import os



def write_key():
    key = input("Type Master Key: ")
    with open('D:/Phyton_Projekt/pythonProject2/key.key', 'wb') as key_file:
        key_file.write(key.encode())
def load_key():
    file = open('D:/Phyton_Projekt/pythonProject2/key.key','rb')
    key = file.read()
    file.close()
    return key


def add():
    nm = input('Account name: ')
    pwd = input('Password: ')
    with open('D:/Phyton_Projekt/pythonProject2/password.txt', 'a+') as f:
        f.write(nm + "-------" + Fernet(load_key()).encrypt(pwd.encode()).decode() + '\n')

def view():
    with open('D:/Phyton_Projekt/pythonProject2/password.txt', 'r+') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("-------")
            print("User:", user, ", Password:", Fernet(load_key()).decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like add,view password, MasterMode or quit? ")
    if mode == "q":
        break
    if mode == "MM":
        if os.path.exists('D:/Phyton_Projekt/pythonProject2/key.key'):
            print("Master Key exist")
            break
        else:
            write_key()
            continue
    if mode == "view":
            print("Only Master can see Dates")
            check_dates = input("Type Master Key: ")
            if check_dates == load_key():
                view()
            else:
                print("Wrong Key!")
                continue
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
