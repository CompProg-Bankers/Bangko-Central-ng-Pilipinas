try:
    with open("bank.txt", "x") as file:
        print("File Successfully Created")
except FileExistsError:
    print("File already exists.")

