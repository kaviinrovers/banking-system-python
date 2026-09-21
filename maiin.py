import random
import datetime

accounts = {}
transactions={}

def create_account():
    name = input("Enter your name: ").strip()
    phone = input("Enter phone number: ").strip()
    pin = input("Create a 4 digit pin: ").strip()
    account_number = random.randint(10000000, 99999999)

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0
    }

    print(f"Account created successfully. Your account number is: {account_number}")

create_account()

def login():
    account_number = int(input("Enter your account number : ").strip())
    pin = input("Enter your pin :").strip()

    if account_number in accounts and accounts[account_number]["pin"] == pin:
        print("Login successful.")
        return account_number
    else:
        print("Invalid account number or pin. please try again.")
        return None

logged_account = login()

def account_menu(account_number):
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.transfer")
    print("5.history")
    print("6.change pin")
    print("7.logout")

    choice = input("Enter your choice :").strip()

    if choice == "1":
        print(f"your balance is : {accounts[account_number]['balance']}")
    elif choice == "2":
        print("Deposit selected")
    elif choice == "3":
        print("withdraw selected")
    elif choice == "4":
        print("transfer selected")
    elif choice == "5":
        print("history selected")
    elif choice == "6":
        print("change pin selected")
    elif choice == "7":
        print("logout selected")
    else:
        print("Invalid choice.Please try again.")

if logged_account is not None:
    account_menu(logged_account)

def account_menu(account_number):
    while True:
        print("1.check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.transfer")
        print("5.history")
        print("6.change pin")
        print("7.logout")
    choice = input("enter your choice :)").strip()

    if choice == "1":
        print(f"Your balance is: {accounts[account_number]['balance']}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        accounts[account_number]['balance'] += amount
        print(f"Deposited {amount}.New balance is: {accounts[account_number]['balance']}")
    