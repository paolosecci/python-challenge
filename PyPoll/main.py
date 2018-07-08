#poll

import pandas as pd
import os
import csv

file_in = os.path.join("election_data.csv")

vote_count = 0
candidates = []
unique_candidates = []
candidate_counts = []
candidate_percentages = []


with open(file_in, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in reader:
        #print(row)

        #The total number of votes cast
        vote_count += 1

        #A complete list of candidates who received votes
        if row[2] not in candidates:
            unique_candidates.append(row[2])
        candidates.append(row[2])

#The total number of votes each candidate won
for cand in unique_candidates:
    candidate_counts.append(candidates.count(cand))

#The percentage of votes each candidate won
for cand_count in candidate_counts:
    candidate_percentages.append(cand_count / vote_count)

max_votes = 0
index = -1
i = 0
#The winner of the election based on popular vote.
for votes in candidate_counts:
    if(max_votes < votes):
        max_votes = votes
        index = i
    i += 1

print("Winner: " + str(unique_candidates[index]))
print("--------------")
for i in range(0, len(unique_candidates)):
    print(str(unique_candidates[i]) + ": " + str(100*candidate_percentages[i]) + "% (" + str(candidate_counts[i]) + ")")
print("--------------")
print("Total Votes: " + str(vote_count) + "\n")




