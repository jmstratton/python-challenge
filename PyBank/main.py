# create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period


#

import os
import csv


# Have the user select which version of the file to use

filename = input ('Please select which version you would like to analize (i.e budget_data_1.csv): ')

# Define Lists and Variables to be calculated

months = []
rev_changes = []

monthcounter = 0
total_revenue = 0
this_month_rev = 0 
last_month_rev = 0
rev_change = 0


# open csv file

PyBankData = os.path.join('raw_data', filename)
with open(PyBankData, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)

#REVENUE - Gather monthly changes in revenue

    for row in csvreader:
        monthcounter = monthcounter + 1
        months.append(row[0])
        this_month_rev = int(row[1])
        total_revenue = total_revenue + this_month_rev
        if monthcounter > 1:
                rev_change = this_month_rev - last_month_rev
                rev_changes.append(rev_change)
        last_month_rev = this_month_rev

#REVENUE CONT'D - Analyze the monthly result

Sum_of_revenue_changes = sum(rev_changes)   #Add all the revenue changes
average_change = Sum_of_revenue_changes / (monthcounter - 1)  #Finds the average change
max_change = max(rev_changes)
min_change = min(rev_changes)
max_monthly_index = rev_changes.index(max_change)
min_monthly_index = rev_changes.index(min_change)
max_month = months[max_monthly_index]
min_month = months[min_monthly_index]

#print results
print('Financial Analysis')
print('---------------------------------------------')
print(f'Total Months: {monthcounter}')
print(f'Total Revenue: ${total_revenue}')
print(f'Average Revenue Change: ${average_change}')
print(f'Greatest Increase in Revenue: {max_month} (${max_change})')
print(f'Greatest Decrease in Revenue: {min_month} (${min_change})')

PyBankText_path = os.path.join ('raw_data', 'Budget_Data_ANALYSIS-CHANGE ME')
#NOTE:  ***THIS FILE WILL BE OVERWRITTEN, RENAME THE FILE FOR FUTURE USE!!!!!***

with open(PyBankText_path, 'w') as newfile:
    newfile.write('Financial Analysis \n')
    newfile.write('---------------------------------------------\n')
    newfile.write(f'Total Months:{monthcounter}' + '\n')
    newfile.write(f'Total Revenue: ${total_revenue}' + '\n')
    newfile.write(f'Average Revenue Change: ${average_change}' + '\n')
    newfile.write(f'Greatest Increase in Revenue: {max_month} (${max_change})' + '\n')
    newfile.write(f'Greatest Decrease in Revenue:  {min_month} (${min_change})' + '\n')