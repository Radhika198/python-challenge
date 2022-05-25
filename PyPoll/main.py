import os
import csv
#Path to collect data from the Resources folder
csv_path=os.path.join("Resources","election_data.csv")

# Open and read csv
with open(csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csv_reader)
    #Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    # Read each row of data after the header
    for row in csv_reader:
        # Skipping empty rows which also helps data cleansing process
        if(len(row)<1):
            continue
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #Number of Votes
    tot_votes = (len(votes))

    #Votes for each Candidate
    for cand in candidates:
        if cand == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif cand == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif cand == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)  
    
    #Each Candidate Percentage of votes on total votes
    khan_percent = round(((khan_votes / tot_votes) * 100),2)
    correy_percent = round(((correy_votes / tot_votes) * 100), 2)
    li_percent = round(((li_votes / tot_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / tot_votes) * 100), 2)
       
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"
    
        #Print Statements

print(f'Election Results'+'\n')
print(f'----------------------------'+'\n')
print(f'Total Votes: {tot_votes}' + '\n')
print(f'-----------------------------------'+'\n')
print(f'Khan: {khan_percent:.3f}% ({khan_votes})' + '\n')
print(f'Correy: {correy_percent:.3f}% ({correy_votes})' + '\n')
print(f'Li: {li_percent:.3f}% ({li_votes})' + '\n')
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})" + '\n')
print(f'-----------------------------------'+ '\n')
print(f'Winner: {winner:}' + '\n')
print(f'-----------------------------------')
