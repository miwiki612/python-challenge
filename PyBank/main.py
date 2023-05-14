
import os

import csv

# in instructor's .py path is with ".." , don't know why doesn't work, mine works with "." 
csvpath = os.path.join(".", "PyBank", "Resources","budget_data.csv")

# read data csv and convert it to list for each column
# convert Profit/Losses column to number, float for currency
with open( csvpath, encoding='UTF-8') as csvfile:
    budget_data = csv.reader( csvfile, delimiter="," )
    
    col_date = []
    col_value = []
    
    for index, row in enumerate(budget_data):
        col_date.append( row[0] )
        if index == 0 :
            col_value.append( row[1] )
        else:
            col_value.append( float( row[1] ) )

# create dictionary for budget data
budget_dict = { col_date[0] : col_date[ 1 : ] ,  col_value[0] : col_value[ 1 : ] } 

# list for result to print
analysis_ls = ["Financial Analysis" , "----------------------------"]

# The total number of months included in the dataset
# unique value in "Date"
n_month  = len(set(budget_dict["Date"]))
analysis_ls.append(  f'Total Months: {n_month}'  )

# The net total amount of "Profit/Losses" over the entire period
# $ format
sum_prf_loss = sum( budget_dict["Profit/Losses"])
analysis_ls.append( f'Total: ${ round( sum_prf_loss,2 )}' )

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# since the data is in date order, change is next month - previous month
monthly_change =[]
for index, row in enumerate( budget_dict["Profit/Losses"][ 0 : -1 ] ) :
    monthly_change.append( budget_dict["Profit/Losses"][ index + 1] - row )
    
avg_monthly_change = sum(monthly_change) / len(monthly_change)
analysis_ls.append( f'Average Change: ${round( avg_monthly_change , 2) }' )

# The greatest increase in profits (date and amount) over the entire period
max_month = budget_dict["Date"][monthly_change.index(max(monthly_change))+1]
analysis_ls.append( f'Greatest Increase in Profits: {max_month} (${round(max(monthly_change),2)})' )

# The greatest decrease in profits (date and amount) over the entire period
min_month = budget_dict["Date"][monthly_change.index(min(monthly_change))+1]
analysis_ls.append( f'Greatest Decrease in Profits: {min_month} (${round(min(monthly_change),2)})' )

# write and print result
analysis_path = os.path.join(".", "PyBank" ,"analysis","budget_analysis.txt")
with open( analysis_path , 'w') as result_txt :
    for i in analysis_ls:
        print(i)
        result_txt.write( i )
        result_txt.write('\n')
    
