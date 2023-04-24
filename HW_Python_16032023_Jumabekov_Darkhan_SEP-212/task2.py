from Store import Store
from Product import Product

def task2():
    store = Store('Ramstore')

    # add 5 random products
    store.rand(5)
    # print all products
    print('\nprint all products \n', store)

    # add 1 product from console
    store.input(1)
    print('\nadd 1 product from console\n', store)

    # print products by price
    from_price = float(input('Enter start price: '))
    to_price = float(input('Enter to price: '))
    print('\nprint products by price\n', store.printProductsByPrice(from_price, to_price))

    # find product by name
    name = input('Enter product name for find: ')
    product = store.findProductByName(name)
    print('\nfind product by name\n', product)

    # find product by manufacturer
    manufacturer = input('Enter manufacturer: ')
    product = store.findProductByManufacturer(manufacturer)
    print('\nfind product by manufacturer\n', product)

    # sort by product name
    print('\nsort by product name\n', *store.sortProductsByName(), sep='\n')

    # sort by product price
    print('\nsort by product price\n', *store.sortProductsByPrice(), sep='\n')

    # add new product
    new_product = Product().rand()
    print('\nnew product:\n', new_product)
    store + new_product
    print('\nadd new product\n', store)

    # delete product
    store - new_product
    print('\ndelete new product\n', store)