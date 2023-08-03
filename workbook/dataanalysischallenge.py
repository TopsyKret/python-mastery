'''
In this exercise, you task is this: write a program to answer the
following three questions:

1. How many bus routes exist in Chicago?

2. How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?

3. What is the total number of rides taken on each bus route?

4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

'''
'''
Solution:

The dataset in use will be ctabus.csv
1. How many bus routes exist in Chicago - we need unique values of the 
   route from all the entries in the dataset

'''
import csv
def read_rides_as_dicts(filename):
    records = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        columns = next(csv_reader)

        for row in csv_reader:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]

            record = {
                'route' : route,
                'date' : date,
                'daytype' : daytype,
                'rides' : rides
                }
            records.append(record)
    
    return records

portfolio = read_rides_as_dicts('filename')
bus_routes = len({s['route'] for s in portfolio})
print(bus_routes)

'''
2. How many people rode the number 22 bus on February 2, 2011?
   What about any route on any date of your choosing?

'''

