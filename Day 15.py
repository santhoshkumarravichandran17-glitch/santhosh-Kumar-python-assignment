class BalanceError(Exception):
    pass

try:
    balance = 500
    withdraw = int(input("Enter amount: "))

    if withdraw > balance:
        raise BalanceError("Insufficient balance")

    print("Transaction successful")

except BalanceError as e:
    print("Error:", e)
