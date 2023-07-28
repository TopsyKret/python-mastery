# total_cost = 0

# file = open('/home/jagriti/Documents/vsc/pythonmastery/python-mastery/Data/portfolio1.dat', 'r')
# for line in file:
#     stock_list = line.split()
#     shares = int(stock_list[1])
#     cost_per_share = float(stock_list[2])
#     total_cost = total_cost + (shares*cost_per_share)

# print(total_cost)
# file.close()

def portfolio_cost(file_path):
    total_cost = 0
    file = open(file_path, 'r')
    for line in file:
        stock_list = line.split()
        try:
          shares = int(stock_list[1])
          cost_per_share = float(stock_list[2])
          total_cost = total_cost + (shares*cost_per_share)
        except ValueError as e:
           print("Couldn't parse", repr(line))
           print("Reason", e)
    return float(total_cost)

print(portfolio_cost('/home/jagriti/Documents/vsc/pythonmastery/python-mastery/Data/portfolio3.dat'))