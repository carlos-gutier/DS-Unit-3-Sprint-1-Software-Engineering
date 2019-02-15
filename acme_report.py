from acme import Product

import random

def generate_products(30):
    product_lst = []
    for _ range(30):
        adjective = random.choice(['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'])
        noun = random.choice(['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???'])
        price_rand = randint(5, 100)
        weight_rand = randint(5, 100)
        flam_rand = random.uniform(0.0, 2.5)
        
        prod = Product(name=f'{adjective} {noun}', price=price_rand, weight=weight_rand, flammability=flam_rand)

    product_lst.append([prod.name, prod.price, prod.weight, prod.flammability])
    
    return product_lst

    return 

def inventory_report(generate_products):
    for each in product_lst:
        names_cnt = len(product_lst)
        avg_price = 

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {names_cnt}')
    print(f'Average price: {}')
    print(f'Average weight: {}')
    print(f'Average flammability: {}')




python
if __name__ == '__main__':
    inventory_report(generate_products())
    

