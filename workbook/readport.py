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

# from pprint import pprint
# pprint(read_portfolio(filename))
# output >> there are multiple entries for certain stock names such as MSFT and IBM

# List/dictionary/set Comprehension: Data manipulation
# Python list comprehnsion provides a much more short syntax for creating a new list based on the values of an exisiting list
'''
newList = [expression for item in iterable if condition == True]

iterable - can be any iterable object like list, tuple, set etc
condition - is optional 
expression - current item in the iteration, but is also the outcome. You can set the outcome to whatever you like
Square brackets
'''
# portfolio = read_portfolio('filename')
# holdings_more_than_100 = [x for x in portfolio if x['shares'] > 100]
'''

# Python dictionary comprehension - {}
'''

# output_dict = [key:value for [key,value] in iterable if (key,value satisfy the condition)]

# zip() method:
# it takes iterable containers(lists, enumerate, dictionary, tuple) and returns a single iterable object, having mapped values from all the containers

'''

# Set Comprehensions - Curly brackets {}
'''

# {var for var in iterable if condition == True} - same as list

'''

# COUNT THE TOTAL SHARES OF EACH STOCK:
'''

# total_shares = {s['shares']: 0 for s in portfolio}
# for s in portfolio:
#     totals[s['name']] += s['shares']

