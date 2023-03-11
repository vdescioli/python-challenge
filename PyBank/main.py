import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data and variables
month = []
profit = []
month_total = 0
profit_total = 0

# open csv file and read header
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    # create lists for months and profit 
    for row in csvreader:
        month.append(row[0])
        month_total += 1
        profit.append(int(row[1])) 
        profit_total = profit_total + int(row[1])

print(f"Total Months:  " + str(month_total))
print(f"Total:  $" + str(profit_total))

