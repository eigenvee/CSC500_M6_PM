from datetime import date


class ShoppingCart:
    def __init__(self, customer_date, customer_name='William Thrall'):
        cart_date = date.today().strftime('%B %-d, %Y') if customer_date == '' else customer_date
        print("\n  {}'s shopping cart created for the date of {}.".format(cust_name, cart_date))
        self.customer_name = customer_name
        self.date = date.today().strftime('%B %-d, %Y') if customer_date == '' else customer_date
        self.cart_items = []

        # ************** test item ********************
        ''
        self.cart_items.append(ItemToPurchase())
        self.cart_items[0].item_name = 'Spam'
        self.cart_items[0].item_description = 'Pink'
        self.cart_items[0].item_price = 99.99
        self.cart_items[0].item_quantity = 99
        ''
        # ************** test item ********************

    def add_item(self, item):
        self.cart_items.append(item)
        print('\n  ADD ITEM')
        self.cart_items[-1].item_name = input('  Enter a name for item: ')
        self.cart_items[-1].item_description = input('  Enter a description for item: ')
        self.cart_items[-1].item_price = float(input('  Enter the unit price for item: '))
        self.cart_items[-1].item_quantity = int(input('  Enter the purchase quantity of item: '))
        print('\n  Item added to cart.')

    def remove_item(self, name):
        item_found = False
        for item in self.cart_items.copy():
            if item.item_name == name:
                item_found = True
                self.cart_items.remove(item)
                break
        if item_found is True:
            print('\n  Item removed.\n')
        else:
            print('\n  Item not found in cart. Nothing removed.\n')

    def modify_item(self, name, option):
        item_found = False
        for item in self.cart_items.copy():
            if item.item_name == name:
                item_found = True
                if option == 'c':
                    item.item_quantity = int(input('  Enter new item quantity: '))
                if option == 'p':  # Assignment doesn't call for 'Change item price' menu option
                    item.item_price = int(input('  Enter new item price: '))
                if option == 't':  # Assignment doesn't call for 'Change item desc' menu option
                    item.item_description = int(input('  Enter new item description: '))
                break
        if item_found is True:
            print('\n  Item modified.\n')
        else:
            print('\n  Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.get_item_cost()
        return total

    def print_total(self, qty):
        if qty == 0:
            print('  SHOPPING CART IS EMPTY')
        else:
            print('  Total Cost: ${:,.2f}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print('  ***************************************************')
        print('  Shopping Cart Item Descriptions\n')
        if not self.cart_items:
            print('  SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                print('  Item: {}    Desc: {}'.format(item.item_name, item.item_description))
        print('  ***************************************************\n')

    def show_cart(self):
        print('  ***************************************************')
        print("  {}'s Shopping Cart - {}\n".format(self.customer_name, self.date))
        for item in self.cart_items:
            item.print_item_cost()
        qty = self.get_num_items_in_cart()
        if qty != 0:
            print('\n  Total Item Quantity: {}'.format(qty))
        self.print_total(qty)
        print('  ***************************************************\n')


class ItemToPurchase:
    def __init__(self):
        self.item_name = 'name'
        self.item_description = 'description'
        self.item_price = float(0)
        self.item_quantity = int(0)

    def print_item_cost(self):
        item_cost = self.item_quantity * self.item_price
        print('  {}: {} @ ${:,.2f} = ${:,.2f}'.format(self.item_name,
                                                      self.item_quantity,
                                                      self.item_price,
                                                      item_cost))

    def get_item_cost(self):
        return self.item_quantity * self.item_price


def print_menu(cart):
    print("""
*****************************************************
*          MENU                                     *
*          a - Add item to cart                     *
*          r - Remove item from cart                *
*          c - Change item quantity                 *
*          d - Show all item descriptions           *    
*          s - Show shopping cart contents          *
*          q - Quit                                 *
*****************************************************
    """)

    option = input('  Choose an option: ')
    if option == 'q':
        return option
    elif option == 'a':
        cart.add_item(ItemToPurchase())
    elif option == 'r':
        print('\n  REMOVE ITEM')
        name = input('  Enter item name: ')
        cart.remove_item(name)
    elif option == 'c':
        print('\n  CHANGE ITEM QUANTITY')
        name = input('  Enter item name: ')
        cart.modify_item(name, option)
    elif option == 'd':
        print('\n  SHOW ITEM DESCRIPTIONS')
        cart.print_descriptions()
    elif option == 's':
        print('\n  SHOW SHOPPING CART')
        cart.show_cart()
    else:
        print('\n*** Enter a valid option. ***')
    return option


cust_name = str(input('\nEnter your name: '))
cust_date = str(input("Enter a date (press Enter to use today's date): "))
shopping_cart = ShoppingCart(cust_date, cust_name)
while (print_menu(shopping_cart) != 'q'):
    pass
