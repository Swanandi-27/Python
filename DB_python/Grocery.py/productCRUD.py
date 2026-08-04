from Gdb import conn,cursor

def add():
    product_id = int(input("Enter Product ID: "))
    name = input("Enter Name: ")
    brand = input("Enter Brand: ")
    mfg_date = input("Enter Manufacturing Date (YYYY-MM-DD): ")
    exp_date = input("Enter Expiry Date (YYYY-MM-DD): ")
    quantity = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))

    cursor.execute("""
        INSERT INTO product
        (product_id, Name, brand, mfg_date, exp_date, quantity, price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (product_id, name, brand, mfg_date, exp_date, quantity, price))

    conn.commit()
    print("Data Inserted Successfully")

def view():
    cursor.execute("select * from product")
    rows=cursor.fetchall()
    print(rows)

def search():
    print("SEARCH")
    print("\n1search by id\n2.search by name\n3.search by brand\n4.exit")
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
            id=int(input("enter ID:"))
            cursor.execute("Select * from product where product_id =?",(id,))
            row=cursor.fetchone()
            print(row)
        case 2:
            name=input("enter product Name:")
            cursor.execute("select * from product where Name = ?",(name,))
            row=cursor.fetchall()
            print(row)
        case 3:
            brand=input("enter brand name:")
            cursor.execute("select * from product where brand = ?",(brand,))
            row=cursor.fetchall()
            print(row)

         
        case 4:
            exit
        case _:
            print("Invalid choice:")


def update():
    product_id = int(input("Enter Product ID: "))

    cursor.execute(
        "SELECT * FROM product WHERE product_id=?",
        (product_id,)
    )

    row = cursor.fetchone()

    if row:
        print("\nUPDATE MENU")
        print("1. Name")
        print("2. Brand")
        print("3. MFG Date")
        print("4. EXP Date")
        print("5. Quantity")
        print("6. Price")

        ch = int(input("Enter your choice: "))

        match ch:
            case 1:
                name = input("Enter New Name: ")
                cursor.execute(
                    "UPDATE product SET Name=? WHERE product_id=?",
                    (name, product_id)
                )

            case 2:
                brand = input("Enter New Brand: ")
                cursor.execute(
                    "UPDATE product SET brand=? WHERE product_id=?",
                    (brand, product_id)
                )

            case 3:
                mfg_date = input("Enter New MFG Date: ")
                cursor.execute(
                    "UPDATE product SET mfg_date=? WHERE product_id=?",
                    (mfg_date, product_id)
                )

            case 4:
                exp_date = input("Enter New EXP Date: ")
                cursor.execute(
                    "UPDATE product SET exp_date=? WHERE product_id=?",
                    (exp_date, product_id)
                )

            case 5:
                quantity = int(input("Enter New Quantity: "))
                cursor.execute(
                    "UPDATE product SET quantity=? WHERE product_id=?",
                    (quantity, product_id)
                )

            case 6:
                price = int(input("Enter New Price: "))
                cursor.execute(
                    "UPDATE product SET price=? WHERE product_id=?",
                    (price, product_id)
                )

            case _:
                print("Invalid Choice")
                return

        conn.commit()
        print("Product Updated Successfully")

    else:
        print("Product Not Found")



def delete():
    product_id = int(input("Enter Product ID: "))

    cursor.execute(
        "SELECT * FROM product WHERE product_id=?",
        (product_id,)
    )

    row = cursor.fetchone()

    if row:
        print("\nProduct Found")
        print(row)

        ch = input("Do you want to delete this product? (y/n): ")

        if ch.lower() == 'y':
            cursor.execute(
                "DELETE FROM product WHERE product_id=?",
                (product_id,)
            )

            conn.commit()
            print("Product Deleted Successfully")
        else:
            print("Deletion Cancelled")

    else:
        print("Product Not Found")




cart = []

def add_to_cart():

    while True:

        product_id = int(input("Enter Product ID: "))

        cursor.execute(
            "SELECT * FROM product WHERE product_id=?",
            (product_id,)
        )

        row = cursor.fetchone()

        if row:

            print("\nPRODUCT DETAILS")
            print(f"Product ID : {row[0]}")
            print(f"Name       : {row[1]}")
            print(f"Brand      : {row[2]}")
            print(f"MFG Date   : {row[3]}")
            print(f"EXP Date   : {row[4]}")
            print(f"Quantity   : {row[5]}")
            print(f"Price      : {row[6]}")

            choice = input("\nDo you want to add this product to cart? (y/n): ")

            if choice.lower() == "y":

                qty = int(input("Enter Quantity: "))

                if qty > row[5]:
                    print("Insufficient Stock")
                    continue

                total = qty * row[6]

                cart.append({
                    "id": row[0],
                    "name": row[1],
                    "brand": row[2],
                    "qty": qty,
                    "price": row[6],
                    "total": total
                })

                # Update stock in database
                new_qty = row[5] - qty

                cursor.execute(
                    "UPDATE product SET quantity=? WHERE product_id=?",
                    (new_qty, product_id)
                )

                conn.commit()

                print("Product Added To Cart Successfully")

            else:
                print("Product Not Added To Cart")

            more = input("Do you want to add more products (y/n): ")

            if more.lower() != "y":
                print("products added sucessfully")
                break

        else:
            print("Product Not Found")


def view_cart():
    if not cart:
        print("Cart is empty")
        return
    print("------CART-------")
    for item in cart:
        print(
            item["id"],
            item["name"],
            item["brand"],
            item["qty"],
            item["price"],
            item["total"]
        )


def generate_bill():

    if not cart:
        print("Cart is Empty")
        return

    subtotal = 0

    print("\n========== BILL ==========")
    print("Name\tQty\tPrice\tTotal")

    for item in cart:

        print(
            f"{item['name']}\t{item['qty']}\t{item['price']}\t{item['total']}"
        )

        subtotal += item["total"]

    gst = subtotal * 0.05
    grand_total = subtotal + gst

    print("\n--------------------------")
    print("Subtotal :", subtotal)
    print("GST (5%) :", gst)
    print("Total    :", grand_total)
    print("==========================")
    print("Thank You For Shopping")