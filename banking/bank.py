# Python Banking App
import os

def deposit():
    # still has bug when adding - amount.
    # will print error message, but still adds to balance.
    # need to fix this.
    print("------------------------------")
    print("Deposit Menu")
    print("------------------------------")
    print("1. Checking")
    print("2. Savings")
    print("3. Back to Main Menu")
    print("------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        print("------------------------------")
        print("Checking Account Deposit")
        print("------------------------------")
        amount = float(input("Enter the amount to deposit into your checking account: "))
        global checking_balance
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            deposit()
        checking_balance += amount
        print("------------------------------")
        print(f"${amount:.2f} has been deposited into your checking account.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
    elif choice == "2":
        os.system('clear')
        print("------------------------------")
        print("Savings Account Deposit")
        print("------------------------------")
        amount = float(input("Enter the amount to deposit into your savings account: "))
        global savings_balance
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            deposit()
        savings_balance += amount
        print("------------------------------")
        print(f"${amount:.2f} has been deposited into your savings account.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
    elif choice == "3":
          os.system('clear')
          return
    else:
        print("------------------------------")
        print("Invalid choice. Please try again.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
        deposit()

def withdraw():
    print("------------------------------")
    print("Withdraw Menu")
    print("------------------------------")
    print("1. Checking")
    print("2. Savings")
    print("3. Back to Main Menu")
    print("------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        print("------------------------------")
        print("Checking Account Withdrawal")
        print("------------------------------")
        amount = float(input("Enter the amount to withdraw from your checking account: "))
        global checking_balance
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            withdraw()
        elif amount > checking_balance:
            print("------------------------------")
            print("Insufficient funds. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            withdraw()
        else:
            checking_balance -= amount
            print("------------------------------")
            print(f"${amount:.2f} has been withdrawn from your checking account.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
    elif choice == "2":
        os.system('clear')
        print("------------------------------")
        print("Savings Account Withdrawal")
        print("------------------------------")
        amount = float(input("Enter the amount to withdraw from your savings account: "))
        global savings_balance
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            withdraw()
        elif amount > savings_balance:
            print("------------------------------")
            print("Insufficient funds. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            withdraw()
        else:
            savings_balance -= amount
            print("------------------------------")
            print(f"${amount:.2f} has been withdrawn from your savings account.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
    elif choice == "3":
        os.system('clear')
        return
    else:
        print("------------------------------")
        print("Invalid choice. Please try again.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
        withdraw()

def show_balance():
    print("------------------------------")
    print("Your current balances are: ")
    print("------------------------------")
    print(f"Checking Balance: ${checking_balance:.2f}")
    print(f"Savings Balance: ${savings_balance:.2f}")
    print("------------------------------")
    any_key = input("Press any key to continue: ")
    os.system('clear')

def transfer():
    print("------------------------------")
    print("Transfer Menu")
    print("------------------------------")
    print("1. Checking to Savings")
    print("2. Savings to Checking")
    print("3. Back to Main Menu")
    print("------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        print("------------------------------")
        print("Checking to Savings Transfer")
        print("------------------------------")
        amount = float(input("Enter the amount to transfer from your checking account: "))
        global checking_balance
        global savings_balance
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            transfer()
        elif amount > checking_balance:
            print("------------------------------")
            print("Insufficient funds. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            transfer()
        else:
            checking_balance -= amount
            savings_balance += amount
            print("------------------------------")
            print(f"${amount:.2f} has been transferred from your checking account to your savings account.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
    elif choice == "2":
        os.system('clear')
        print("------------------------------")
        print("Savings to Checking Transfer")
        print("------------------------------")
        # global checking_balance
        # global savings_balance
        amount = float(input("Enter the amount to transfer from your savings account: "))
        if amount < 0:
            print("------------------------------")
            print("Invalid amount. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
            transfer()
        elif amount > savings_balance:
            print("------------------------------")
            print("Insufficient funds. Please try again.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
        else:
            savings_balance -= amount
            checking_balance += amount
            print("------------------------------")
            print(f"${amount:.2f} has been transferred from your savings account to your checking account.")
            print("------------------------------")
            any_key = input("Press any key to continue: ")
            os.system('clear')
    elif choice == "3":
        os.system('clear')
        return
    else:
        print("------------------------------")
        print("Invalid choice. Please try again.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
        transfer()


# def main_menu():
#     print("Welcome to the Banking App!")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Transfer")
#     print("5. Savings")
#     print("6. Checking")
#     print("7. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         deposit()
#     elif choice == "2":
#         withdraw()
#     elif choice == "3":
#         check_balance()
#     elif choice == "4":
#         transfer()
#     elif choice == "5":
#         savings()
#     elif choice == "6":
#         checking()
#     elif choice == "7":
#         is_running = False
#     else:
#         print("Invalid choice. Please try again.")


checking_balance = 0
savings_balance = 0
is_running = True
os.system('clear')

while is_running:
    # main_menu()
    print("------------------------------")
    print("Welcome to the Banking App!")
    print("------------------------------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    print("------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        show_balance()
    elif choice == "2":
        os.system('clear')
        deposit()
    elif choice == "3":
        os.system('clear')
        withdraw()
    elif choice == "4":
        os.system('clear')
        transfer()
    elif choice == "5":
        is_running = False
    else:
        print("------------------------------")
        print("Invalid choice. Please try again.")
        print("------------------------------")
        any_key = input("Press any key to continue: ")
        os.system('clear')
print("------------------------------")
print("Thank you for using the Banking App!")
print("------------------------------")
