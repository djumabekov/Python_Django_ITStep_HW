from DB import DB
from Store import Store
from Product import Product

def task2():
    db = DB("Store")
    store = Store('Ramstore', db)

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
    product = store.findProductByParam(name, 'Name')
    print('\nfind product by name\n', product)

    # find product by manufacturer
    manufacturer = input('Enter manufacturer: ')
    product = store.findProductByParam(manufacturer, 'Manufacturer')
    print('\nfind product by manufacturer\n', product)

    # sort by product name
    print('\nsort by product name\n', store.sortProductsByParam('Name'), sep='\n')

    # sort by product price
    print('\nsort by product price\n', store.sortProductsByParam('Price'), sep='\n')

    # add new product
    new_product = Product().rand()
    print('\nnew product:\n', new_product)
    store + new_product
    print('\nadd new product\n', store)

    # delete product
    store - new_product
    print(f'\ndelete new product:\n', store)

    # delete product by id
    print('\ndelete product by id:')
    id = input("Enter product id: ")
    store.deleteById(id)
    print(f'\ndelete product with id "{id}":\n', store)