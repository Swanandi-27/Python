store = {
    "spices": {
        "turmeric": {"price": 50, "quantity": 100, "unit": "100g", "mfg": "01-01-2026", "exp": "01-01-2027"},
        "chilli": {"price": 40, "quantity": 80, "unit": "100g", "mfg": "02-01-2026", "exp": "02-01-2027"},
    },
    "biscuits": {
        "oreo": {"price": 30, "quantity": 50, "unit": "pack", "mfg": "10-06-2026", "exp": "10-12-2026"},
        "goodday": {"price": 20, "quantity": 60, "unit": "pack", "mfg": "05-06-2026", "exp": "05-12-2026"},
    },
    "dryfruits": {
        "almond": {"price": 200, "quantity": 40, "unit": "1kg", "mfg": "01-05-2026", "exp": "01-05-2027"},
        "cashew": {"price": 300, "quantity": 30, "unit": "1kg", "mfg": "02-05-2026", "exp": "02-05-2027"},
    }
}

cart = []

while True:

    
    
    print("         WELCOME TO DMART")
    print("1. Grocery Section")
    print("2. View Bill")
    print("3. Exit")
    

    choice = input("Enter your choice: ")

    match choice:

        
        case "1":
            while True:
                print("\n GROCERY SECTION")
                print("1. Spices")
                print("2. Biscuits")
                print("3. Dry Fruits")
                print("4. Back")

                sub_choice = input("Enter your choice: ")

                
                match sub_choice:
                    case "1":
                        print("\n Available Spices:")
                        for item, data in store["spices"].items():
                            print(item, "=>", data)

                        product = input("Enter spice name: ")

                        if product in store["spices"]:
                            qty = int(input("Enter quantity: "))

                            if qty <= store["spices"][product]["quantity"]:
                                price = store["spices"][product]["price"] * qty
                                cart.append((product, qty, price))

                                store["spices"][product]["quantity"] -= qty
                                print("Added to cart ")
                            else:
                                print(" Not enough stock!")
                        else:
                            print(" Item not found!")

                    
                    case "2":
                        print("\n Available Biscuits:")
                        for item, data in store["biscuits"].items():
                            print(item, "=>", data)

                        product = input("Enter biscuit name: ")

                        if product in store["biscuits"]:
                            qty = int(input("Enter quantity: "))

                            if qty <= store["biscuits"][product]["quantity"]:
                                price = store["biscuits"][product]["price"] * qty
                                cart.append((product, qty, price))

                                store["biscuits"][product]["quantity"] -= qty
                                print("Added to cart ")
                            else:
                                print(" Not enough stock!")
                        else:
                            print(" Item not found!")

                    
                    case "3":
                        print("\n Available Dry Fruits:")
                        for item, data in store["dryfruits"].items():
                            print(item, "=>", data)

                        product = input("Enter dry fruit name: ")

                        if product in store["dryfruits"]:
                            qty = int(input("Enter quantity: "))

                            if qty <= store["dryfruits"][product]["quantity"]:
                                price = store["dryfruits"][product]["price"] * qty
                                cart.append((product, qty, price))

                                store["dryfruits"][product]["quantity"] -= qty
                                print("Added to cart ")
                            else:
                                print(" Not enough stock!")
                        else:
                            print(" Item not found!")

                    
                    case "4":
                        break

                more = input("Do you want to continue shopping? (yes/no): ")
                if more.lower() != "yes":
                    break

        
        case "2":
            print("\n FINAL BILL")
            total = 0

            if len(cart) == 0:
                print("Cart is empty!")
            else:
                for item in cart:
                    print("Product:", item[0], "| Qty:", item[1], "| Price:", item[2])
                    total += item[2]

                
                print("TOTAL BILL =", total)
                

        
        case "3":
            print(" Thank you for shopping at DMART!")
            break

        
        case _:
            print(" Invalid choice! Try again.")