correct_pin = 1234
balance = 10000
pin = int(input("Enter your PIN: "))
if pin == correct_pin:
    print("PIN CORRECT")
    print(f"Your balance is: ₹{balance}")

    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw <= balance:
        print("withdrawal allowed")
        balance = balance-withdraw
        print(f"Your remaining balance is:{balance}")
    else:
        print("insufficient balance")

else:
    print("INCORRECT PIN")
