# File: Project3.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date Created: 04/21/24
# Description of Program: This assignment involves building an online shopping utility where users can browse, search, add, and remove products from a database of cheese products.

import csv

class Product:
    def __init__(self, sku, company, description, price):
        self._sku = sku
        self._company = company
        self._description = description
        self._price = price

    def __str__(self):
        return f"{self._sku}: ${self._price:.2f} {self._company} {self._description}"

class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, product):
        self._items.append(product)

    def remove_item(self, sku):
        for item in self._items:
            if item._sku == sku:
                self._items.remove(item)
                return True
        return False

    def total_cost(self):
        return sum(item._price for item in self._items)

def build_database(filename):
    database = {}
    sku_counter = 1

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 3 and not row[0].startswith("#"):
                company, description, price = row
                price = float(price)
                product = Product(sku_counter, company, description, price)
                database[sku_counter] = product
                sku_counter += 1

    return database

def help_command():
    print("The following commands are available:")
    print("   Help      - show this message;")
    print("   Exit      - exit this application;")
    print("   Brands    - list the brands available;")
    print("   Search    - look for products by brand and/or by description keywords;")
    print("   Add       - add a product to your shopping cart by Sku number;")
    print("   Remove    - remove a product from your shopping cart by Sku number;")
    print("   Cart      - display the current contents of your shopping cart;")
    print("   Checkout  - purchase the contents of your shopping cart.\n")

def brands_command(database):
    brands = set(product._company.lower() for product in database.values())
    print("Available brands:")
    i=0
    for brand in sorted(brands):
        if i != len(brands)-1:
            print(brand.title(), end=", ")
        else:
            print(brand.title() + ".")
        i+=1
             
    print()


def search_command(database):
    brand = input("  Brand (or return for any brand): ").lower()
    keywords = input("  Product keywords (or return for any): ").lower().split()

    matching_products = []
    for product in database.values():
        if (not brand or brand in product._company.lower()) and all(keyword in product._description.lower() for keyword in keywords):
            matching_products.append(product)

    if matching_products:
        print("\nFound the following matching products:")
        for product in matching_products:
            print(f"  {product}")
    else:
        print("No matching products located.")
    print()

def add_command(database, cart):
    sku = int(input("  Enter product Sku to add to cart: "))
    
    product = database.get(sku)
    if product:
        cart.add_item(product)
        #print("Product added to cart.")
        print()
    else:
        print(f"No product with Sku {sku} found.")

def remove_command(cart):
    sku = int(input("  Enter product Sku to remove from cart: "))
    
    if cart.remove_item(sku):
        #print("\nProduct removed from cart.\n")
        print()
    else:
        print(f"No product with Sku {sku} found.\n")

def cart_command(cart):
    print("Your shopping cart contains:\n")
    for item in cart._items:
        print(f"  {item}")
    print(f"Cart contains {len(cart._items)} items, for a total cost of ${cart.total_cost():.2f}\n")

def checkout_command(cart):
    print("You have purchased the following items:")
    for item in cart._items:
        print(f"  {item}")
    print(f"Summary: {len(cart._items)} items for a total cost of ${cart.total_cost():.2f}\n")
    print("Thanks for shopping with us! Please come back soon.\n")

def main():
    filename = input("Enter data filename: ")
    try:
        database = build_database(filename)
    except FileNotFoundError:
        print(f"Cannot find file: {filename}")
        return

    cart = ShoppingCart()

    print(f"\nWelcome to the online shopping app. We have a large selection of cheeses")
    print("available from many popular brands. Happy shopping!\n")

    while True:
        command = input("Enter a command (help, exit, brands, search, add, remove, cart, checkout): ").strip().lower()
        print()
        if command == "help":
            help_command()
        elif command == "exit":
            print("Thanks for shopping with us! Please come back soon.\n")
            break
        elif command == "brands":
            brands_command(database)
        elif command == "search":
            search_command(database)
        elif command == "add":
            add_command(database, cart)
        elif command == "remove":
            remove_command(cart)
        elif command == "cart":
            cart_command(cart)
        elif command == "checkout":
            checkout_command(cart)
            break
        else:
            print("Sorry, your command wasn't recognized. Try again.\n")

if __name__ == "__main__":
    main()
