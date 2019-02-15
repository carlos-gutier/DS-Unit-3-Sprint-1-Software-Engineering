#python
#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        prod = Product('Tester', 19, 8, 0.8)
        self.assertEqual(prod.stealability(), "Very stealable!")
    
    def test_explode(self):
        prod = Product('Tester', 19, 8, 0.8)
        self.assertEqual(prod.explode(), "...fizzle.")



class AcmeReportTests(unittest.TestCase):
    
    def test_default_num_products(self):
        """Checking that that list of length 30"""
        prod_lst = generate_products(30)
        self.assertEqual(len(prod_lst), 30)

    def test_legal_names(self):
        '''Checks that the generated names for a
        default batch of products are all valid'''
        from itertools import product
        combos = list(product(ADJECTIVES, NOUNS))
        name_combos = [' '.join(combos[i]) for i in range(len(combos))]
        prod_lst = generate_products(30)
        name_lst = [x[0] for x in prod_lst]
        self.assertTrue(name_combos, name_lst)


if __name__ == '__main__':
    unittest.main()