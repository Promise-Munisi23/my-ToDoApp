import csv
import questionary
import typer

app = typer.Typer()

@app.command()
def sign_up():
    user_email = input("Enter your email: ")
    user_password = questionary.password('Enter your password: ').ask()
    save_info_in_csv(user_email, user_password)
    
@app.command()
def login():
    email = input("Enter your email: ")
    password = questionary.password('Enter your password: ').ask()
    
    if authenticate_user(email, password):
        print("Login successful!")
    else:
        print("Invalid credentials")


def save_info_in_csv(user_email, user_password):
    with open('login.csv', 'w', newline='') as file:
        user_details = [{'user_email': user_email, 'user_password': user_password}]
        writer = csv.DictWriter(file, fieldnames=['user_email', 'user_password'])
        writer.writeheader()
        for data in user_details:
            writer.writerow(data)
        print('Data has been added to the CSV file')

def read_info_in_csv():
    with open('login.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def authenticate_user(user_email, user_password):
    users = read_info_in_csv()
    for user in users:
        if user['user_email'] == user_email and user['user_password'] == user_password:
            return True
    return False



if __name__== '__main__':
    app()
    save_info_in_csv()