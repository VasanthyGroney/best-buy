# Setup initial stock of inventory
def start(store):
    while True:
        print("Store Menu")
        print("==========")

        choice = input(int("Please choose a number: "))

        if choice == 1:
            store.list_all_product()
            print("1. List all products in store")
        elif choice == 2:
            store.show_total_amount()
            print("2. Show total amount in store.")
        elif choice == 3:
            store.make_an_oder()
            print("3. Make an order.")
        elif choice == 4:
            print("4. Quit")
            break
        else:
            print("Error with your choice! Try again!")

    return  # Exit the function when the loop is finished


# Call the start function to begin the program

