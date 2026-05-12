from datetime import datetime #IMPORT DATE

now = datetime.now()
date = now.strftime("%Y-%m-%d %H:%M:%S")

#MAKE FILE
try:
    with open("bank.txt", "x") as file:
        print("File Successfully Created")
except FileExistsError:
    print("File already exists.")


from datetime import datetime

#DEPOSIT MONEY
def depositMoney():
    amount = float(input("Enter amount:    "))
    with open("bank.txt", "a") as file:
        file.write(f"Deposit: {amount} on ({date})\n")
    print(f"Deposit: {amount} on ({date})")
    
    