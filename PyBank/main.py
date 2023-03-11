import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data and variables
month = []
profit = []
monthly_change = []
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

    # create monthly change list and find min and max 
    for i in range(1, len(profit)):
        monthly_change.append(profit[i] - profit[i-1])

    # add index to find month of respective change    
    g_inc_index = monthly_change.index(max(monthly_change))
    g_dec_index = monthly_change.index(min(monthly_change))        

    # find average change 
    avg_change = sum(monthly_change) / len(monthly_change)           

print("  ")
print("Financial Analysis")
print("----------------------------------")
print("Total Months:  " + str(month_total))
print("Total:  " + '${:.0f}'.format(profit_total))
print("Average Change:  " + '${:.2f}'.format(avg_change))
print("Greatest Increase in Profits:  ",month[g_inc_index + 1], '(${:.0f})'.format(max(monthly_change)))
print("Greatest Decrease in Profits:  ", month[g_dec_index+1], '(${:.0f})'.format(min(monthly_change)))
print(" ")

# write to txt file  
analysis_path = os.path.join("..", "Analysis", "results.txt")
with open(analysis_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------\n")
    txtfile.write("Total Months:  " + str(month_total)+ "\n" )
    txtfile.write("Total:  " + '${:.0f}'.format(profit_total)+"\n")
    txtfile.write("Average Change:  " + '${:.2f}'.format(avg_change)+"\n")
    txtfile.write("Greatest Increase in Profits:  " + month[g_inc_index + 1] + '  (${:.0f})'.format(max(monthly_change))+"\n")
    txtfile.write("Greatest Decrease in Profits:  " + month[g_dec_index+1] + '  (${:.0f})'.format(min(monthly_change))+"\n")
