nips_stock = 15
collection = 0

while nips_stock >= 0:
    print(f'Balance: {nips_stock}')
    print(f'Current Collection: ${collection}')
    purchase_command = input('Do you want to buy: y/n ')
    if purchase_command == 'y':
        nips_stock = nips_stock - 1
        collection = collection + 2
        if nips_stock == 0:
            print('Out of stock')
            print(f'Total collection: ${collection}')
            break
    elif purchase_command == 'n':
        break
    else:
        print('Wrong command')
