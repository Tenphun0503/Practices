import pizzaReceipt as pr

SIZE = ['S', 'M', 'L', 'XL']
NO = ['NO', 'Q', 'N']
YES = ['YES', 'Y']
TOPLIST = []


def order_pizza():
    while True:
        size = input("Choose size").upper()
        if size not in SIZE:
            print("wrong size input, try again")
        else:
            break

    toppings = []
    while True:
        topping = input("LIST to show topping\tX to stop adding").upper()
        if topping == 'X':
            break
        elif topping == 'LIST':
            print(TOPLIST)
        elif topping not in TOPLIST:
            print("we don't have " + topping + ", try again")
        else:
            toppings.append(topping)

    return size, toppings


if __name__ == "__main__":
    aPizza = input("Do u want?").upper()
    pizza = ''
    if aPizza in NO:
        print('Thank you')
    elif aPizza in YES:
        pizza = [order_pizza()]
        while True:
            continueOrder = input("do u wanna more?").upper()
            if continueOrder in NO:
                break
            elif continueOrder in YES:
                pizza.append(order_pizza())
            else:
                print("wrong input")

    pr.generateReceipt(pizza)


