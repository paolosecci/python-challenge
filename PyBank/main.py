#bank

import pandas as pd
import os
import csv

file_in = os.path.join("budget_data.csv")

month_count = 0
net_flux = 0
current_max_delta = ["", "0"]
current_min_delta = ["", "0"]

with open(file_in, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in reader:
        #print(row)
        
        #the total number of months included in the dataset
        month_count += 1
        
        #the total net amount of "Profit/Losses" over the entire period
        net_flux += int(row[1])

        #the greatest increase in profits (date and amount) over the entire period
        if(int(row[1]) > int(current_max_delta[1])):
            current_max_delta = row

        #the greatest decrease in losses (date and amount) over the entire period
        if(int(row[1]) < int(current_min_delta[1])):
            current_min_delta = row

#the average change in "Profit/Losses" between months over the entire period
average_change_per_month = net_flux / month_count


#summary
outString = ''

outString+= 'FINANCIAL ANALYSIS\n'
outString+= '-----------------------\n'

outString+= ("Total Months: "			+ str(month_count) + '\n')
outString+= ("Net Flux: $"			+ str(net_flux) + '\n')
outString+= ("Average Change (per month): $"	+ str(average_change_per_month) + '\n')
outString+= ("Greatest Account Increase: "	+ str(current_max_delta[0]) + " $" + str(current_max_delta[1]) + '\n')
outString+= ("Greatest Account Decrease: "	+ str(current_min_delta[0]) + " $" + str(current_min_delta[1]) + '\n')

print(outString)

textfile = open('output.txt', 'w')
textfile.write(outString)
textfile.close()
