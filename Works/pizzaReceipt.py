"""
a function for generating receipt
"""
def generateReceipt(pizzaOrder):
    # Dictionary of base price and additional cost
    base_price = {'S':7.99, 'M':9.99, 'L':11.99, 'XL': 13.99}
    add_price = {'S': 0.5, 'M': 0.75, 'L': 1.00, 'XL': 1.25}

    if pizzaOrder == '':
        print('You did not order anything')
    else:
        print("Your order: ")
        prices = []
        for id, pizza in enumerate(pizzaOrder):
            num = 0
            if len(pizza[1]) > 3:
                num = len(pizza[1]) - 3
            price = base_price[pizza[0]] + num * add_price[pizza[0]]
            print("Pizza" + str(id + 1) + ":" + pizza[0] + "\t\t" + str(price))
            for topping in pizza[1]:
                print("- " + topping)

            prices.append(price)
        total = sum(prices)
        tax = total * 0.13
        total_with_tax = total + tax
        print("Tax:\t\t" + str(tax))
        print("Total:\t\t" + str(total_with_tax))