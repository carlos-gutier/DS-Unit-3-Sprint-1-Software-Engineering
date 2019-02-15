#!/usr/bin/env python
class Product():

    '''
    `name` (string with no default)
    `price` (integer with default value 10)
    `weight` (integer with default value 20)
    `flammability` (float with default value 0.5)
    `identifier` (integer, automatically genererated as a random (uniform) number 
    anywhere from 1000000 to 9999999, inclusive)
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        
        '''Calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"'''

        s_ratio = self.price / self.weight

        if s_ratio < 0.5:
            return "Not so stealable..."
        elif 1 > s_ratio >= 0.5:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        
        '''Calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.", if it is
        greater or equal to 10 but less than 50 return "...boom!", and otherwise
        return "...BABOOM!!'''

        e_ratio = self.flammability * self.weight

        if e_ratio < 10:
            return "...fizzle."
        elif 50 > e_ratio >= 10:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    def __init__(self, name, price=10, flammability=0.5):
        super(BoxingGlove, self).__init__(name, price=10, weight=10, flammability=0.5)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 15 > self.weight >= 5:
            return "Hey that hurt!"
        else:
            return "OUCH!"


