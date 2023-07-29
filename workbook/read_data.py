import csv

def read_rides_as_tuples(filename):
    '''
    Type 1: Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        # create a csv reader object
        csv_reader = csv.reader(f)

        # extracting field names through the first row, Skipping headers
        fields = next(csv_reader)

        # extracting row data, one by one - Loop
        for row in csv_reader:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            # creating a tuple of the record in a tuple called record
            record = (route, date, daytype, rides)
            # append the tuple to the list
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Type 2: Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        fields = next(csv_reader)

        for row in csv_reader:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            # Create a dictionary of the record in dictionary called record
            record = {
                'route' : route,
                'date' : date,
                'daytype' : daytype,
                'rides' : rides
                }
            records.append(record)
    return records

class Row:
    # When we create objects for classes, it requires memory and the attributes are stored in the form of a dictionary
    # More the objects, more the memory space taken
    # slots reduces the sixe of objects. It is a concept of memory optimiztion
    # It allocates space for a fixed amount of attributes - reduces wastage of memeory space and speeds up the program
    __slots__ = ['route', 'date', 'daytype', 'rides']
    '''
    Type 3: Define a class with __slot__
    '''
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# namedtuple - type of dictionaries container
# Like dictionaries, it contains keys associated with values
# Difference - It supports access from both key-value and iteration(index) that dictionaries lack
 
from collections import namedtuple
Row = namedtuple('Row', ('route', 'date', 'daytype', 'rides'))

def read_rides_as_instances(filename):
    records = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        fields = next(csv_reader)
        for row in csv_reader:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':

    # Following is the basic structure of using the tracemalloc module:
    import tracemalloc
    tracemalloc.start()
    # function call
    app = read_rides_as_instances("/home/jagriti/Documents/vsc/pythonmastery/python-mastery/Data/ctabus.csv")
    print('Memory Use: Current %d, Peak: %d' % tracemalloc.get_traced_memory())


