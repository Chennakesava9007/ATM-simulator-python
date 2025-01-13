import time

print("=======Welcome to the ATM=======")
time.sleep(1)
print("=======Please insert your CARD=======")
time.sleep(2)

password = 9007
pin = int(input("Please enter your 4 digit pin : "))
balance = 5457
transaction_history = []

if pin == password:
        while True:
            print("\n========== ATM Menu ==========")
            print("""choose an option :
                    1. Check Balance
                    2. Withdraw Cash
                    3. Deposit Cash
                    4. Change PIN
                    5. Transaction History
                    6. Exit""")
            choice = input("Enter your choice (1-6): ")
            
            
            if choice == '1':
                # Check Balance
                print(f"Current Balance: {balance}")
                
                
            elif choice == '2':
                # Withdraw Cash
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount > 0 and balance >= amount:
                        balance -= amount
                        transaction_history.append(f'Withdrawal:{amount}')
                        print(f"Withdrawn: {amount}")
                        print(f"Current Balance: {balance}")
                    else:
                        print("Withdrawal failed. Insufficient balance.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
                    
                    
            elif choice == '3':
                # Deposit Cash
                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount > 0:
                        balance += amount
                        transaction_history.append(f'Deposit: {amount}')
                        print(f"Deposited: {amount}")
                        print(f"Current Balance: {balance}")
                    else:
                        print("Deposit failed. Please enter a valid amount.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
                    
                    
            elif choice == '4':
                # Change PIN
                new_pin = input("Enter new PIN (4 digits): ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("Invalid PIN. Please enter 4 digits.")
                    
                    
            elif choice == '5':
                # Transaction History
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
                    
                    
            elif choice == '6':
                # Exit
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and6.")
else:
    print("Wrong pin please try again")
  

  #                             or                          #
  #      Another code for ATM to increase readability       #


import time
def atm_menu():
    return ("============ATM MENU============"
            "\n 1.Check balance"
            "\n 2.withdraw cash"
            "\n 3.Deposit cash"
            "\n 4.Change pin"
            "\n 5.Transaction history"
            "\n 6.Exit")
def Check_balance(balance):
    print(f"Current Balance: {balance}")
def Withdraw_cash(balance,transaction_history):
    try:
        amount=float(input("Enter the withdraw amount: "))
        if amount>0 and amount<=balance:
            balance-=amount
            print(f"Withdraw amount : {amount}")
            print(f"Current balance : {balance}")
            transaction_history.append(f"withdrawn cash : {amount}")
        else:
            print("Withdral failed, Insufficient balance")
    except ValueError:
        print("Enter the valid amount, type correctly")
    return balance

def Deposit_cash(balance,transaction_history):
    try:
        amount=float(input("Enter the deposit cash :"))
        if amount>0:
            balance+=amount
            transaction_history.append(f"Deposited Cash: {amount}")
            print(f"Deposited Cash: {amount}")
            print(f"Current balance: {balance}")
        else:
            print("Insufficent balance! ")
    except ValueError:
        print("Invalid input! Enter the valid amount")
    return balance
def change_pin():
    try:
        new_pin=input("Enter the '4' digits pin:")
        if len(new_pin)==4 and new_pin.isdigit():
            print("Pin was changed sucessfully")
        else:
            print("Invalid input! pls enter the '4 digits pin ")
    except ValueError:
        print("Invalid input pls enter the digits")
    return None

def Check_transaction_history(transaction_history):
    print("Transaction History: ")
    if transaction_history:
        print("\n".join(transaction_history))
    else:
        print("No transaction found")

def atm():
    print("=========== Welcome To ATM ==========")
    time.sleep(1)
    print("Please insert the card")
    time.sleep(2)
    
    password="9007"
    pin=input("Enter the 4 digits pin: ")
    balance=5000
    transaction_history=[]

    if pin==password:
        while True:
            print(atm_menu())
            choice=input("Enter your choice (1-6): ")

            if choice=="1":
                Check_balance(balance)
            elif choice == '2':
                balance = Withdraw_cash(balance, transaction_history)
            elif choice == '3':
                balance = Deposit_cash(balance, transaction_history)
            elif choice == '4':
                new_pin = change_pin()
                if new_pin:
                    pin = new_pin
            elif choice == '5':
                Check_transaction_history(transaction_history)
            elif choice == '6':
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    else:
        print("Wrong pin. Please try again.")
if __name__=="__main__":
    atm()
