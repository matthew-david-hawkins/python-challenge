# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#Import dependencies
import os
import csv


#%%
#Define the path to the dataset
csv_path = "Resources/election_data.csv"


#%%
#Initialize
voters = 0
candidates = []
votes = []
percentages = []


#%%
#Read the data set into a csv reader object
with open(csv_path, newline='') as csv_file:

    #Define reader object delimited by ","
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Define the header
    csv_header = next(csv_reader)
    
#     #print the Head
#     print(csv_header)
#     for i in range(6):
#         print(next(csv_reader))
    
    #iterate over the lines in the csv_file
    for rows in csv_reader:
        
        #sum the votor IDs
        voters = voters +1
        
        #Define the cadidate
        candidate = rows[2]
        
        #if the current candidate is not in the list, add there name and append the vote count list
        if (candidate in candidates) == False:
            candidates.append(candidate)
            votes.append(0)
            percentages.append(0)
        
        #--------------------------------------------
        #Increment the candidate's vote count
        #--------------------------------------------

        # Iterate over the indices of the candidates list
        for i in range(len(candidates)):
            
            #increase the candidate's vote count
            if (candidate == candidates[i]):
                votes[i] = votes[i] + 1

#%%
#Calculate the vote percentages for each candidate
# Iterate over the indices of the candidates list
for i in range(len(candidates)):
        percentages[i] = votes[i] / voters * 100


#%%
#Determine the candidate with the highest number of votes
winner = candidates[votes.index(max(votes))]


#%%
#Define messages
messages = []
messages.append("Election Results")
messages.append("--------------------------------")
messages.append(f"Total votes: {voters}")
messages.append("--------------------------------")
for i in range(len(candidates)):
    messages.append(f"{candidates[i]}: {round(percentages[i], 4)}%  ({votes[i]})")
messages.append("--------------------------------")
messages.append(f"Winner: {winner}")
messages.append("--------------------------------")


#%%
#print messages to the terminal
print("")
for message in messages:
    print(message)


#%%
#create an output folder if one doesn't already exist
try:
    os.mkdir("Output")
except OSError:
    print ("Matt's Warning: Creation of the directory 'Output' failed")


#%%
#Export the analysis to a text file
with open("Output/election_results.txt", 'w+') as output:
    for message in messages:
        output.write(message)
        output.write("\n")


#%%



