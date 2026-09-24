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
        "balance": 0,
        "history": []
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
    while True:
        print("1.check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.transfer")
        print("5.history")
        print("6.change pin")
        print("7.logout")

        choice = input("enter your choice :").strip()

        if choice == "1":
            print(f"Your balance is: {accounts[account_number]['balance']}")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            accounts[account_number]['balance'] += amount
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            accounts[account_number]['history'].append(f"{timestamp} - Deposit - {amount}")
            print(f"Deposited {amount}. New balance is: {accounts[account_number]['balance']}")
        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            if amount <= accounts[account_number]['balance']:
                accounts[account_number]['balance'] -= amount
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                accounts[account_number]['history'].append(f"{timestamp} - Withdraw - {amount}")
                print(f"Withdraw {amount}. New balance is: {accounts[account_number]['balance']}")
            else:
                print("Insufficient balance")
        elif choice == "4":
            amount = float(input("Enter transfer amount: "))
            if amount <= accounts[account_number]['balance']:
                receiver_account = int(input("Enter receiver account number: ").strip())
                if receiver_account in accounts:
                    accounts[account_number]['balance'] -= amount
                    accounts[receiver_account]['balance'] += amount
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    accounts[account_number]['history'].append(f"{timestamp} - Transfer to {receiver_account} - {amount}")
                    accounts[receiver_account]['history'].append(f"{timestamp} - Transfer from {account_number} - {amount}")
                    print("Transfer successful.")
                else:
                    print("Receiver not found.")
            else:
                print("Insufficient balance.")
        elif choice == "5":
            hist = accounts[account_number].get('history', [])
            if not hist:
                print("No transactions yet.")
            else:
                print("Transaction history:")
                for item in hist:
                    print(item)
        elif choice == "6":
            old_pin = input("Enter old PIN: ").strip()
            if old_pin == accounts[account_number]['pin']:
                new_pin = input("Enter new PIN: ").strip()
                confirm_pin = input("Confirm new PIN: ").strip()
                if new_pin == confirm_pin:
                    accounts[account_number]['pin'] = new_pin
                    print("PIN changed successfully.")
                else:
                    print("New PIN and confirmation do not match.")
            else:
                print("Old PIN incorrect.")
        elif choice == "7":
            print("logout selected")
            break
        else:
            print("Invalid choice.Please try again.")

if logged_account is not None:
    account_menu(logged_account)
