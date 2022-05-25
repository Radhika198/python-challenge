#import budget data 
import os
import csv 

#Path to collect data from the Resources folder
csvpath=os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header row first
    csv_header = next(csvreader)
    rows_list = list(csvreader)
    
    #Declaring variables
    month = []
    revenue = []
    rev_change = []
    Avg_change = []
                   
    # Read through each row of data after the header and count number of months    
    for row in rows_list:
         # Skipping empty rows which also helps data cleansing process
        if(len(row) < 1):
               continue
        # Appending months(column 1) into month variable
        month.append(row[0])
        # Appending revenue(column 2) into revenue variable
        revenue.append(row[1])

    #Sum of Revenue 
    rev_int = map(int,revenue)
    tot_revenue = (sum(rev_int))
  
    # Average Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        # append profit_loss
        rev_change.append(profit_loss)
    Total = sum(rev_change)
    # Calculate Average change
    Avg_change = Total / len(rev_change)

#Greatest Increase
    profit_increase = max(rev_change)
    k = rev_change.index(profit_increase)
    mon_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(rev_change)
    j = rev_change.index(profit_decrease)
    mon_decrease = month[j+1]

#Print Outcome
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total months: " + str(len(month)))
print("Total: $" + str(tot_revenue)) 
print(f'Average Change: ${Avg_change:.2f}')
print(f"Greatest Increase in Profits: {mon_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {mon_decrease} (${profit_decrease})")
