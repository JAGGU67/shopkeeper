# Adding chocolates
def add_chocolates(chocolates):
    name = input("Enter a name of chocolate: ")
    amount = int(input("Enter an amount: "))
    stock = int(input("Enter a stock: "))
    chocolates.append({"name": name, "amount": amount, "stock": stock})
    return chocolates
 # Adding chocolates
def add_chocolates(chocolates):
    name = input("Enter a name of chocolate: ")
    amount = int(input("Enter an amount: "))
    stock = int(input("Enter a stock: "))
    chocolates.append({"name": name, "amount": amount, "stock": stock})
    return chocolates

# Removing sold stock
def remove_chocolates(chocolates, name, quantity):
    for chocolate in chocolates:
        if chocolate["name"] == name:
            if quantity <= chocolate["stock"]:
                chocolate["stock"] -= quantity
                return chocolates
            else:
                print("Not enough stock available.")
                return chocolates
    print("Chocolate not found.")
    return chocolates

# Updating chocolate amount
def update_chocolates(chocolates):
    name = input("Enter a name of chocolate: ")
    amount = int(input("Enter a new amount: "))
    for chocolate in chocolates:
        if chocolate["name"] == name:
            chocolate["amount"] = amount
            return chocolates
    print("Chocolate not found.")
    return chocolates

# Updating stock
def update_stock(chocolates):
    name = input("Enter a name of chocolate: ")
    stock = int(input("Enter a new stock: "))
    for chocolate in chocolates:
        if chocolate["name"] == name:
            chocolate["stock"] = stock
            return chocolates
    print("Chocolate not found.")
    return chocolates

# Selling stock items
def buy(chocolates):
    name = input("Enter a name of chocolate: ")
    quantity = int(input("Enter the number of quantities: "))
    total_amount = 0
    for chocolate in chocolates:
        if chocolate["name"] == name:
            if quantity <= chocolate["stock"]:
                chocolate["stock"] -= quantity
                total_amount = quantity * chocolate["amount"]
                print(f"Total amount: {total_amount}")
                return chocolates, total_amount
            else:
                print("Not enough stock available.")
                return chocolates, 0
    print("Chocolate not found.")
    return chocolates, 0
