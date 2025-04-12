from store_2 import store
from product_2_step_2 import *


def menu_header(header):
    return header


def menu_options(options_list):
    return options_list


def user_input(user_choice):
    return input(user_choice)


def list_of_items(store):
    products = store.get_all_products()
    if not products:
        print("No active products available in the store.")
        return []
    else:
        print("Available products:")
        for ind, product in enumerate(products):
            print(f"{ind + 1}. {product}")
    return products

def add_to_shopping_list(bb_store):
    shopping_list = []
    while True:
        products = bb_store.get_all_products()
        if not products:
            break

        print("Enter 0 to finish adding products to the shopping list")
        try:
            product_index = int(input("Enter number of the product you want to add to your shopping list: "))
            if product_index == 0:
                break
            elif 1 <= product_index <= len(products):
                selected_product = products[product_index - 1]

                if isinstance(selected_product, NonStockedProduct):
                    print(f"{selected_product.name} added to shopping list.")
                    shopping_list.append((selected_product, 1))
                else:
                    quantity = int(input(f"Enter quantity of '{selected_product.name}' to add: "))
                    if quantity <= 0:
                        print("Enter a positive number")
                        continue
                    if quantity > selected_product.quantity:
                        print(f"Only {selected_product.quantity} available in the store. Select smaller amount.")
                        continue
                    shopping_list.append((selected_product, quantity))
                    print(f"Added {quantity} of '{selected_product.name}' to your shopping list.\n")
            else:
                print("Invalid number, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
    return shopping_list


def main():
    header_string = f"Store Menu\n{'-' * len('Store Menu')}"
    menu_list = (
        f"1. List all products in store\n"
        f"2. Show total amount in store\n"
        f"3. Make an order\n"
        f"4. Quit"
    )
    user_string = "Please choose a number: "
    while True:
        header_menu = menu_header(header_string)
        options_menu = menu_options(menu_list)

        print(header_menu)
        print(options_menu)
        input_user = user_input(user_string)

        if input_user == "1":
            list_of_items(store)
        elif input_user == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity of all products in the store: {total_quantity}")
        elif input_user == "3":
            shopping_list = add_to_shopping_list(store)
            if shopping_list:
                total_price = store.order(shopping_list)
                print(f"Total price of order: ${total_price}")
            else:
                print("No items were added to the shopping list.")
        elif input_user == "4":
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please select again.")


if __name__ == "__main__":
    main()