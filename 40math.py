import math
number = 12.66

print(math.sqrt(25))
print(math.floor(10.9))
print(math.ceil(10.1))
print(math.pow(10,2))
print(math.factorial(5))





balance = 1000.0  # Initial balance
    
print("Welcome to Simple Bank ATM!")
    
while True:
    print("\nPlease select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
        
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print(f"Your current balance is: ${balance:.2f}")
        
    elif choice == 2:
        deposit_amount = float(input("Enter amount to deposit: $"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Successfully deposited ${deposit_amount:.2f}. Your new balance is ${balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
        
    elif choice == 3:
            withdrawal_amount = float(input("Enter amount to withdraw: $"))
            if withdrawal_amount > balance:
                print("Insufficient funds. Please try a smaller amount.")
            elif withdrawal_amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                balance -= withdrawal_amount
                print(f"Successfully withdrew ${withdrawal_amount:.2f}. Your new balance is ${balance:.2f}.")
        
    elif choice == 4:
            print("Thank you for using Simple Bank ATM. Goodbye!")
            break
        
    else:
            print("Invalid choice. Please try again.")

