import getpass
import csv

def sign_up():
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    login_information = read_info_in_csv()

def save_info_in_csv(login_information):
    with open('login.csv', 'w', newline='') as file:
        user_details = ['email', 'password']
        writer = csv.DictWriter(file, user_details=user_details)
        writer.writeheader()
        for email, password in login_information.items():
            writer.writerow({'email': email, 'password': password})

def read_info_in_csv():
    with open('login.csv', 'r') as file:
        reader = csv.DictReader(file)
        return {'email': 'password'}
    return {}

