def order_management():
    product_orders = []
    while True:
        product_name = input("Product Name: ")
        product_price = int(input("Price: "))
        product_quantity = int(input("Quantity: "))

        total_amount = product_price * product_quantity
        product_orders.append ((product_name, product_price, product_quantity, total_amount))

        # Ask the user if they want to add a product
        add_product = input("Do you want to add another item? (y/n): ")
        if add_product != 'y':
            break

    # Customer details
    customer_name = input("\nCustomer Name: ")

    # Ensure proper handling for Senior ID input.  we used typecast to convert the string to int
    senior_citizen_id = input("Senior ID No (blank if not senior citizen): ")

    # Calculate total and apply the discount
    grand_total = sum(product[3] for product in product_orders)  # sum total_amounts

    if senior_citizen_id:
        discount = grand_total * 0.10
        grand_total -= discount #used to apply a discount to the grand total
        

    # Final print
    for product in product_orders:
        print(f"\nItem: {product[0]}, Price: {product[1]}, Quantity: {product[2]}, Total Amount: {product[3]}")
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No: {senior_citizen_id}")
    print(f"Grand Total: {grand_total}")

order_management()
