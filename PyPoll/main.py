import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

# List for candiadtes, dictionary for votes, and variables
candidates = []
v_per_cand = {}
percentage = {}
vote_total = 0

# open csv file and read header
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    # count total votes first 
    for row in csvreader:
        vote_total += 1
        
        # create list for candidates and count votes per candidate 
        if row[2] not in candidates:
            candidates.append(row[2])
            v_per_cand[row[2]] = 0
        v_per_cand[row[2]] += 1
    
    # calculate percentage of total votes 
    for i in candidates:
        percentage[i] = v_per_cand[i]/vote_total
        
        
print(vote_total)
print(candidates)
print(v_per_cand)
print(percentage)