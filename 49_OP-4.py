# Create a Restaurant class that stores menu items in a dictionary and prints the bill.

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.total_bill = 0

    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price

    def print_bill(self, ordered_items):
        print("Bill Details:")
        for item in ordered_items:
            if item in self.menu:
                price = self.menu[item]
                self.total_bill += price
                print(f"{item}: ${price:.2f}")
            else:
                print(f"{item}: Not on menu")
        print(f"Total Bill: ${self.total_bill:.2f}")

# Example usage
restaurant = Restaurant()
restaurant.add_menu_item("Pasta", 12.50)
restaurant.add_menu_item("Pizza", 15.00)
restaurant.add_menu_item("Salad", 8.00)
restaurant.print_bill(["Pasta", "Salad"])