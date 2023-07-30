# DATA
'''
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

'''
import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        # Removing headers 
        fields = next(csv_reader)

        for row in csv_reader:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

# Using pprint - pretty print
# This module provides the the capability to pretty print arbitrary python data structures in well-formatted way
'''
from pprint import pprint
pprint(read_portfolio(filename))
'''
# List Comprehension:
# Python list comprehnsion provides a much more short syntax for creating a new list based on the values of an exisiting list
'''
newList = [expression for item in iterable if condition == True]
'''