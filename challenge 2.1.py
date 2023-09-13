class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than 0."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("123456789", "John Doe", 1000)

    # Test deposit and withdrawal
    print(my_account.deposit(500))
    print(my_account.withdraw(200))
    print(my_account.withdraw(1500))  # Should display "Insufficient funds for withdrawal."
    
    # Display account balance
    print(my_account.display_balance())
