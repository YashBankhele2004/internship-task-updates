import datetime

# Transaction Class
class Transaction:
    def __init__(self, transaction_type, amount, fee=0):
        self.transaction_type = transaction_type
        self.amount = amount
        self.fee = fee
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Account Class
class Account:
    def __init__(self, account_number, user_name, account_type, balance=0):
        self.account_number = account_number
        self.user_name = user_name
        self.account_type = account_type
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount, fee_percentage=0.01):
        fee = amount * fee_percentage
        self.balance += (amount - fee)
        self.log_transaction("Deposit", amount, fee)
        print(f"Deposit successful. A fee of ${fee:.2f} has been applied. New balance: ${self.balance:.2f}")

    def withdraw(self, amount, fee=1, overdraft_limit=0):
        if self.account_type == "Savings" and self.balance < amount:
            print("Insufficient funds for withdrawal.")
            return
        elif self.account_type == "Checking" and self.balance + overdraft_limit < amount:
            print("Exceeds overdraft limit.")
            return
        
        self.balance -= (amount + fee)
        self.log_transaction("Withdrawal", amount, fee)
        print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

    def transfer(self, target_account, amount):
        if self.balance < amount:
            print("Insufficient funds for transfer.")
            return
        self.balance -= amount
        target_account.balance += amount
        self.log_transaction("Transfer (Out)", amount)
        target_account.log_transaction("Transfer (In)", amount)
        print("Transfer successful!")

    def log_transaction(self, transaction_type, amount, fee=0):
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "fee": fee,
            "balance": self.balance
        }
        self.transaction_history.append(transaction)

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"User Name: {self.user_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# User Class
class User:
    def __init__(self, name, address, pin):
        self.name = name
        self.address = address
        self.pin = pin
        self.accounts = []
        self.login_attempts = 0

    def login(self, entered_pin):
        if self.login_attempts >= 3:
            print("Account locked. Too many failed login attempts.")
            return False
        if entered_pin == self.pin:
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            print("Incorrect PIN.")
            return False

    def add_account(self, account):
        self.accounts.append(account)

# Bank Class
class Bank:
    def __init__(self):
        self.users = []
        self.account_counter = 1000

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def create_account(self, user, account_type, initial_deposit):
        if account_type == "Savings" and initial_deposit < 100:
            print("Minimum deposit for savings account is $100.")
            return None
        
        self.account_counter += 1
        new_account = Account(self.account_counter, user.name, account_type, initial_deposit)
        user.add_account(new_account)
        print(f"Account created successfully! Account Number: {self.account_counter}")
        return new_account

# Main Program
def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Advanced Bank Management System!")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            pin = input("Set a 4-digit PIN: ")
            user = User(name, address, pin)
            bank.add_user(user)
            print("User registered successfully!")

        elif choice == "2":
            name = input("Enter your name: ")
            user = bank.find_user(name)
            if not user:
                print("User not found.")
                continue

            pin = input("Enter your PIN: ")
            if user.login(pin):
                print(f"Welcome, {user.name}!")
                while True:
                    print("\n1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. View Account Details")
                    print("6. Logout")
                    action = input("Choose an action: ")

                    if action == "1":
                        acc_type = input("Enter account type (Checking/Savings): ")
                        initial_deposit = float(input("Enter initial deposit amount: "))
                        bank.create_account(user, acc_type, initial_deposit)
                    
                    elif action in ["2", "3", "4", "5"]:
                        if not user.accounts:
                            print("No accounts found. Create an account first.")
                            continue
                        account = user.accounts[0]  # Selecting the first account
                    
                        if action == "2":
                            amount = float(input("Enter deposit amount: "))
                            account.deposit(amount)
                        elif action == "3":
                            amount = float(input("Enter withdrawal amount: "))
                            account.withdraw(amount)
                        elif action == "4":
                            print("Feature coming soon!")
                        elif action == "5":
                            account.display_account_details()
                    elif action == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
