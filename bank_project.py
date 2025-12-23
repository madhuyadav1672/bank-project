class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        self.debit_card_applied = False

    def add_money(self, amount):
        self.balance += amount
        print(f"Added {amount} to account {self.account_number}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def apply_debit_card(self):
        self.debit_card_applied = True
        print("Debit card application submitted.")

    def check_debit_card_status(self):
        if self.debit_card_applied:
            return "Debit card application approved."
        else:
            return "Debit card not applied yet."


class SBIAccount(BankAccount):
    def __init__(self, account_number, balance, customer_name):
        super().__init__(account_number, balance, customer_name)
        print(f"SBI Account created for {customer_name} with account number {account_number}")


# Example usage
if __name__ == "__main__":
    # Assuming existing customer account data
    existing_account = SBIAccount("1234567890", 5000.0, "John Doe")

    # Customer adds money
    existing_account.add_money(2000.0)

    # Show current balance
    print(f"Current balance: {existing_account.get_balance()}")

    # Apply for debit card
    existing_account.apply_debit_card()

    # Check debit card status
    print(existing_account.check_debit_card_status())
