#choclates stock and price
chocolates = [
    {"name": "vanilla", "amount": 50, "stock": 100},
    {"name": "chocolate", "amount": 30, "stock": 500},
    {"name": "strawberry", "amount": 80, "stock": 800},
    {"name": "butterscotch", "amount": 95, "stock": 700},
]

def owner_use(chocolates):
    while True:
        print("\nOwner Menu:")
        print("1. Add Quantity")
        print("2. Update Quantity")
        print("3. Update Stock")
        print("4. Exit")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            add_chocolates(chocolates)
        elif choice == 2:
            update_chocolates(chocolates)
        elif choice == 3:
            update_stock(chocolates)
        elif choice == 4:
            print("Exited Owner Menu.")
            break
        else:
            print("Enter a valid choice.")

def customer_use(chocolates):
    while True:
        print("\nCustomer Menu:")
        print("1. Buy Chocolate")
        print("2. Exit")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            buy(chocolates)
        elif choice == 2:
            print("Exited Customer Menu.")
            break
        else:
            print("Enter a valid choice.")

flag = True
while flag:
    print("\nCandy Shop")
    print("1. Owner Use")
    print("2. Customer Purpose")
    print("3. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        owner_use(chocolates)
    elif choice == 2:
        customer_use(chocolates)
    elif choice == 3:
        print("Exited Candy Shop.")
        flag = False
    else:
        print("Enter a valid choice.")