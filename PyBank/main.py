# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
#Overview:
# In this challenge, you are tasked with creating a Python script for 
# analyzing the financial records of your company. You will give a 
# set of financial data called budget_data.csv. The dataset is composed 
# of two columns: Date and Profit/Losses.

#Calculate: 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#References:
# Creating directories https://stackabuse.com/creating-and-deleting-directories-with-python/


#%%
#Import Dependencies
import csv

import os


#%%
# Define the path to the dataset
csv_path = "Resources/budget_data.csv"


#%%
#initialize
months = 0
account = 0
greatest_loss = 0
greatest_profit = 0
greatest_loss_month =""
greatest_profit_month =""


#%%
# Read the dataset into a file stream objects
with open(csv_path, newline='') as csv_file:
    
    #Define reader object delimited by ","
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Define the header
    csv_header = next(csv_reader)
    #print(csv_header)
    
    #Loop over the number of lines
    for row in csv_reader:
        
        #Sum the months
        months = months + 1
        
        #Define the current profit/loss
        pl = int(row [1])
        
        #Sum the Profit/losses
        account = account + pl
        
        #track the greatest profit by comparing current profit to greatest profit
        if pl > greatest_profit:
            greatest_profit_month = row[0]
            greatest_profit = pl
            
        #track the greatest loss by comparing current loss to greatest loss
        elif pl < greatest_loss:
            greatest_loss_month = row[0]
            greatest_loss = pl
        
        #print(f"{row}  months = {months}  account = {account} greatest profit = {greatest_profit} greatest loss = {greatest_loss}")
        #print(greatest_loss_month)


#%%
#Calculate the average profit and loss
mean_pl = account / months
mean_pl


#%%
#Define messages
messages = []
messages.append("Finanacial Analysis")
messages.append("-------------------------------------------------------------------------")
messages.append(f"Total Months: {months}")
messages.append(f"Total: ${account}")
messages.append(f"Average Change: ${round(mean_pl,2)}")
messages.append(f"Greatest Increase in Profits: {greatest_profit_month} ({greatest_profit})")
messages.append(f"Greatest Decrease in Profits: {greatest_loss_month} ({greatest_loss})")


#%%
#print messages to the terminal
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
with open("Output/financial_analysis.txt", 'w+') as output:
    for message in messages:
        output.write(message)
        output.write("\n")


