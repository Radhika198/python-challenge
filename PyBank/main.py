import os
import csv
import sys 

#Path to collect data from the Resources folder
csvpath=os.path.join('Resources','budget_data.csv')

# Open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read the header row first
    csv_header = next(csvreader)

    rows_list = list(csvreader)
    
    #Declaring variables
    months = []
    profit_and_loss = []
    profit_loss_change = []
    Avg_change = []
                   
    # Read through each row of data after the header and count number of months    
    for row in rows_list:
         # Skipping empty rows which also helps data cleansing process
        if(len(row) < 1):
               continue
        # Appending months into months variable
        months.append(row[0])
        # Appending profit and loss  into profit and loss variable
        profit_and_loss.append(row[1])

    #Calculate Total value of profit and loss 
    profit_loss_int = map(int,profit_and_loss)
    total_profit_and_loss = (sum(profit_loss_int))
  
    # Calculate Average Change value of profit and loss
    i = 0
    for i in range(len(profit_and_loss) - 1):
        profit_loss_diff = int(profit_and_loss[i+1]) - int(profit_and_loss[i])
        # append profit_loss
        profit_loss_change.append(profit_loss_diff)
    Total = sum(profit_loss_change)
    Avg_change = Total/len(profit_loss_change)

    #Determine Greatest Increase in Profits
    greatest_profit_increase = max(profit_loss_change)
    k = profit_loss_change.index(greatest_profit_increase)
    month_of_increase = months[k+1]
    
    #Determine Greatest Decrease in Losses
    greatest_loss_decrease = min(profit_loss_change)
    j = profit_loss_change.index(greatest_loss_decrease)
    month_of_decrease = months[j+1]

results=sys.stdout
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total months: " + str(len(months)))
print("Total: $" + str(total_profit_and_loss)) 
print(f'Average Change: ${Avg_change:.2f}')
print(f"Greatest Increase in Profits: {month_of_increase} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {month_of_decrease} (${greatest_loss_decrease})")

with open('Analysis/financial_analysis.txt', 'w') as text:
    sys.stdout=text

#Print Outcome of Financial Analysis
    print(f'Financial Analysis'+'\n')
    print(f'----------------------------'+'\n')
    print("Total months: " + str(len(months)))
    print("Total: $" + str(total_profit_and_loss)) 
    print(f'Average Change: ${Avg_change:.2f}')
    print(f"Greatest Increase in Profits: {month_of_increase} (${greatest_profit_increase})")
    print(f"Greatest Decrease in Profits: {month_of_decrease} (${greatest_loss_decrease})")

   
#Exporting the Financial analysis result into text file
    sys.stdout=results
#with open('Analysis/financial_analysis.txt', 'w') as text:
    #text.write(f'Financial Analysis'+'\n')
    #text.write(f'----------------------------'+'\n')
    #text.write("Total months: " + str(len(months))+'\n')
    #text.write("Total: $" + str(total_profit_and_loss)+'\n') 
    #text.write(f'Average Change: ${Avg_change:.2f}'+'\n')
    #text.write(f"Greatest Increase in Profits: {month_of_increase} (${greatest_profit_increase})"+'\n')
    #text.write(f"Greatest Decrease in Profits: {month_of_decrease} (${greatest_loss_decrease})")
