import os
import csv
import operator


#Assign the variables
total_votes = 0
candidates = {}



#Path to collect data from the Resources folder & open CSV file
CSVpath = os.path.join('Resources', 'election_data.csv')
with open(CSVpath, 'r', newline = '') as csvfile:
    election_data = csv.reader(csvfile, delimiter= ',')

    #Skip the header row
    next(election_data, None)

    #Calculate the total number of votes cast; 
    #Gather a complete list of candidates who received votes;
    #Calculate the total number of votes each candidate won
    for row in election_data:

        
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        else:
            candidates[row[2]] = candidates[row[2]] + 1

    total_votes = 0

    for votes in candidates.values():
        total_votes = total_votes + votes

    
  

    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------")

#Path to export file as textfile
export_file = os.path.join('Resources', "election_data.txt")
with open(export_file, 'w', newline='') as textfile:
    textfile.write("Election Results" "\n")
    textfile.write("--------------------------" "\n")
    textfile.write("Total Votes: " + str(total_votes) + "\n")
    textfile.write("--------------------------" "\n")
 

    #Calculate the percentage of votes each candidate won
    for name, votes in candidates.items():
        percent= round((votes/total_votes) * 100, 3)
        percentage = "{:.3}".format(percent)
        print(name + " " + percentage + "% " + "(" + str(votes) + ")")
        textfile.write(name + " " + percentage + "% " + "(" + str(votes) + ")" + "\n")
        

#Winner based on popular vote 
    print("--------------------------")
    textfile.write("--------------------------" "\n")
    winner = max(candidates.items(), key=operator.itemgetter(1))[0]
    print("Winner: " + winner)
    textfile.write("Winner: " + winner)
   
        

