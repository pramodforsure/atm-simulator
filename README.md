# ATM Simulator

A beginner-friendly Python program that simulates a basic ATM withdrawal process using PIN verification, balance checking, and conditional statements.

## About the Project

I am a freshman undergraduate learning Python. This project is part of my beginner programming practice and focuses on user input, variables, `if/else` conditions, comparisons, and updating values.

## What the Program Does

The program:

1. Stores a PIN and starting balance.
2. Asks the user to enter their PIN.
3. Checks whether the PIN is correct.
4. Displays the current balance when the PIN is correct.
5. Asks for a withdrawal amount.
6. Checks whether enough balance is available.
7. Deducts the withdrawal amount when it is allowed.
8. Displays the remaining balance.
9. Shows an error message for an incorrect PIN or insufficient balance.

## Concepts Used

* `input()`
* `int()`
* Variables
* `if / else`
* Comparison operators
* Arithmetic operations
* Updating variables
* f-strings
* Nested conditions

## Code

```python
correct_pin = 1234
balance = 10000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("PIN CORRECT")
    print(f"Your balance is: ₹{balance}")

    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw <= balance:
        print("withdrawal allowed")
        balance = balance - withdraw
        print(f"Your remaining balance is:{balance}")
    else:
        print("insufficient balance")

else:
    print("INCORRECT PIN")
```

## Example

```text
Enter your PIN: 1234
PIN CORRECT
Your balance is: ₹10000
Enter amount to withdraw: 2500
withdrawal allowed
Your remaining balance is:7500
```

## Requirements

* Python 3.x
* No external libraries

## How to Run

Run the program from a terminal:

```bash
python "atm simulator.py"
```

Then enter the PIN and withdrawal amount when prompted.

## Learning Status

**Level:** Beginner
**Project Type:** Python Practice Project
**Focus:** Conditions, nested conditions, user input, arithmetic, and variable updates

## Future Improvements

* Add deposit functionality.
* Add balance inquiry.
* Add multiple withdrawal attempts.
* Add input validation.
* Create a menu-driven ATM.
* Use functions to organize the ATM operations.
* Add transaction history.

## Author

A freshman undergraduate learning Python and developing programming fundamentals through hands-on projects.
