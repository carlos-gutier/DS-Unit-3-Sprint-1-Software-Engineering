from acme import Product

import random
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
def generate_products(n=30):
    product_lst = []
    for _ in range(n):
        adj_rand = random.choice(ADJECTIVES)
        noun_rand= random.choice(NOUNS)
        price_rand = random.randint(5, 100)
        weight_rand = random.randint(5, 100)
        flam_rand = random.uniform(0.0, 2.5)
        
        prod = Product(name=f'{adj_rand} {noun_rand}', price=price_rand, weight=weight_rand, flammability=flam_rand)
        product_lst.append([prod.name, prod.price, prod.weight, prod.flammability])
    
    return product_lst

def inventory_report(product_lst):
    for x in product_lst:
        names_cnt = len(set([x[0] for x in product_lst]))
        avg_price = sum ([x[1] for x in product_lst]) / len(product_lst)
        avg_weight = sum ([x[2] for x in product_lst]) / len(product_lst)
        avg_flam = sum ([x[3] for x in product_lst]) / len(product_lst)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {names_cnt}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flam}')




#python
if __name__ == '__main__':
    inventory_report(generate_products())
    

