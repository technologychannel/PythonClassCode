class BankAccount:
    def __init__(self, name, phone, balance=0.00):
        self.name = name
        self.phone = phone
        self.balance =balance

    def deposit(self, amount):
        if amount >=0:
            self.balance += amount
            print(f"Successful deposit Rs {amount:.2f} to {self.name} account")
        else:
            print("Invalid Deposit Amount")
    
    def withdraw(self, amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs {amount:.2f} from {self.name}'s account.")
        else:
            print("Invalid Withdraw Amount or Insufficient Balance")

    def get_amount(self):
        return f"{self.name}'s current balance: Rs {self.balance:.2f}"


ram = BankAccount("Ram Thapa","99898989")
ram.deposit(5000)
ram.withdraw(1000)

print(ram.get_amount())


hari = BankAccount("Hari Sharma", "39839823")
hari.deposit(500)
print(hari.get_amount())
