class Beverage:
    """ ABC class component """
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        """ Info """
        return self.description

    def cost(self):
        """ summ """
        price = float()
        return price


class CondimentDecorator(Beverage):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def get_description(self):
        old = super().get_description()
        self.description = old + ', ' + self.obj.description
        return self.description



# a = CondimentDecorator()
# print(a.description)
# print(a.get_description())

# Base

class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        price = 100.0
        return price


class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'DarkRoast'

    def cost(self):
        price = 40.0
        return price

# Additives

class Milk(CondimentDecorator):
    def __init__(self, obj):
        super().__init__(obj)
        self.description = 'Milk'

    def get_description(self):
        return super().get_description()
    
    def cost(self):
        pass


class Sugar(CondimentDecorator):
    def __init__(self, obj):
        super().__init__(obj)
        self.description = 'Sugar'

    def get_description(self):
        return super().get_description()
    
    def cost(self):
        pass
   

coffe = Espresso()
print(coffe.description)

coffe = Sugar(coffe)
print(coffe.get_description())

coffe = Sugar(coffe)
print(coffe.get_description())

coffe = Milk(coffe)
print(coffe.get_description())