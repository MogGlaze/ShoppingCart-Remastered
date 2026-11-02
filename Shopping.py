products = { ## Total list of products
    "Banana" :5.00,
    "Gummy" :3.99,
    "MilkShake" : 2.99,
    "HotPocket" : 3.99,
    "Chair" : 1.00
}
shopping_cart = {} ## Shopping cart

def display_products(): ### Function for displaying products
    print("Available Items")
    # Display products with a numbered list for easy selection
    for index, (item, price) in enumerate(products.items(), 1):
        print(f"{index}. {item} - ${price:.2f}")
        
    print()

def add_product():
    product_keys = list(products.keys())
    display_products()
    product_number = int(input("What Product (enter number): "))
    
    # Map number to dictionary key
    if 1 <= product_number <= len(product_keys):
        item = product_keys[product_number - 1]
    else:
        print("Invalid product number!")
        return
        
    quantity = -1
    while quantity < 0:
        quantity = int(input(f"How many {item}s do you want? "))
    
    # Add or update the item in the shopping cart dictionary
    shopping_cart[item] = shopping_cart.get(item, 0) + quantity
    
    print(f"{quantity} {item}s have been added")
    print(f"{item} total quantity in cart is now {shopping_cart[item]}")
    
    
    
def remove_product():
    if not shopping_cart:
        print("Your cart is empty!")
        return
    print("YOUR SHOPPING CART!!!")
    cart_items = list(shopping_cart.keys())
    for i, item in enumerate(cart_items, 1):
        print(f"{i}. {item} ({shopping_cart[item]})")
        
    remove_num = int(input("What item number would you like to remove?: "))
    if 1 <= remove_num <= len(cart_items):
        item_to_remove = cart_items[remove_num - 1]
        removed_qty = shopping_cart.pop(item_to_remove)
        print(f"{item_to_remove} has been removed from your cart")
    else:
        print("Invalid item number!")

def view_cart():
    print("YOUR SHOPPING CART!!")
    if not shopping_cart:
        print("Your cart is empty!")
    for item, quantity in shopping_cart.items():
        print(f"{item}: {quantity}")
    print()

def shopping_total(): 
    print("CURRENT TOTAL")
    subtotal = 0
    for item, quantity in shopping_cart.items():
        price = products[item] * quantity ### Gets the price directly from the products dictionary
        
        print(f"{item} (x{quantity}): ${price:.2f}")
        subtotal += price
    
    print(f"Subtotal: ${subtotal:.2f}")
    return subtotal

def checkout(subtotal):
    
    if(subtotal < 10.00): ## Determines what the subtotal qualifies
        discount = 0.00
    elif(10.00 <= subtotal < 20.00):
        discount = 0.05
    elif(20.00 <= subtotal < 40.00):
        discount = 0.10
    else:
        discount = 0.15
    
    final_total = subtotal - subtotal * discount
    print("CHECKOUT")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount * 100}%")
    print(f"Amount Saved: ${subtotal * discount:.2f}")
    
    print(f"Final Total: ${final_total:.2f}")
    print("Thank you for shopping!")
    return final_total
    
        
    

option = 0
sub = 0.0
while(option != 6):  ### Starting menu
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    
    option = int(input("Enter your choice: ")) ## Selects choice
    
    if(option == 1): ## Displays
        print()
        display_products()
    
    elif(option == 2): ## adds
        print()
        add_product()
    
    elif(option == 3): ## Removes
        print()
        remove_product()
    
    elif(option == 4): ## VIEWING
        print()
        view_cart()
    
    elif(option == 5): ### SHOPPING TOTAL
        print()
        sub = shopping_total()
    
    elif(option == 6): ### CHECKOUT
        print()
        sub = shopping_total() # ensures subtotal is current
        print()
        checkout(sub)
    
    else:
        print("Please make a valid option")