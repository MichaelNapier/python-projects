MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter amount to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Invalid input. Please enter a number.")
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("Enter amount to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a number.")
    return amount

def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet ${total_bet}. Your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    # Spin the slot machine
    # Display the result
    # Update the balance

main()