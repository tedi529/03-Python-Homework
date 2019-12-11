# This script opens a csv file and analyses election data contained within

# Modules
import os
import csv
import operator

# Path to collect data from election_data.csv
election_csv = os.path.join("election_data.csv")

# Initialize variables
total_votes_cast = 0
candidates_total = []
candidate_votes = {}
candidate_percent = {}

# Open CSV
with open(election_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip first row
    next(csvreader)
    
    # Iterate through row in data
    for row in csvreader:
        
        # Count total votes cast counting each row as a vote
        total_votes_cast += 1

        # Append to candidates total list
        candidate_name = row[2]
        
        if candidate_name not in candidates_total:
            candidates_total.append(candidate_name)   
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
            
# Calculate % won by each candidate
for key, value in candidate_votes.items():
    candidate_percent[key] = round((value/total_votes_cast)*100,3)
    
# Determine the winner
winner = max(candidate_votes.items(), key=operator.itemgetter(1))[0]

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total votes: {total_votes_cast}")
print("-------------------------")
for key, value in candidate_votes.items():
    print(f"{key}: {candidate_percent[key]}% ({value})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
results = open("elections_results.txt", "w+")
results.write("Election Results \n")
results.write("------------------------- \n")
results.write(f"Total votes: {total_votes_cast} \n")
results.write("------------------------- \n")
for key, value in candidate_votes.items():
    results.write(f"{key}: {candidate_percent[key]}% ({value}) \n")
results.write("------------------------- \n")
results.write(f"Winner: {winner} \n")
results.write("------------------------- \n")