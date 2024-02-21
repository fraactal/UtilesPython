import csv
from icecream import ic


# Save a CSV file of your transactions in the same folder as this project and put the name below
FILE = 'snakes_count_10.csv'

def finance_manager(file):
    sum = 0 
    transactions = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            #get "Game Number", "Game Length","date","Boolean"
            name = row[0]
            amount = float(row[2])
            date = row[3]
 
            transaction = (date, name, amount)
            sum += amount
            transactions.append(transaction)
    print(f"The sum {sum}")
    print('')
    return transactions


def output_to_file(text):
    with open('debug_log_csv.txt','a') as f:
        f.write(text + '\n')


# change the configuration of icecream loging, in this case, we get the output file log
ic.configureOutput(prefix='Debug| ',outputFunction=output_to_file,
                   includeContext=True)


ic(finance_manager(FILE))

