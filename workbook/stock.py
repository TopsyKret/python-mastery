class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    

# String operators:
'''

'%s is smaller than %s' % ('one', 'two')

print("Mr. %s, the total is %.2f." % ("Jekyll", 15.53))

place = "New York"
print("Welcome to %s!" % place)


'''