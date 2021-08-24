#Import needed libraries
import os
import csv

#Read the CSV file
csv_path = os.path.join('Resources','budget_data.csv')
with open (csv_path) as csvfile:
    budget_data = csv.reader(csvfile, delimiter = ',')

    #Skip the header of the CSV file
    csv_header = next(budget_data)

    #Iterate through the rest of the rows to get all required values
    total_months = 0
    total = 0
    previous_profit = 0
    changes = []
    months = []
    for row in budget_data:
        total_months += 1
        total += int(row[1])
        changes.append(int(row[1])-int(previous_profit))
        months.append(row[0])
        previous_profit = row[1]

    #As there is nothing prior to the first month, the first change and its corresponding month need to be removed
    changes.remove(changes[0])
    months.remove(months[0])

    #Determine average of change in profits/losses
    change_average = round((sum(changes)/len(changes)),2)
    
    #Determine the greatest increase in profit (maximum value in changes list)
    max_inc = max(changes)
    max_inc_month = months[changes.index(max_inc)]
    
    #Determine the greatest decrease in losses (minimum value in changes list)
    max_dec = min(changes)
    max_dec_month = months[changes.index(max_dec)]
#Print all of the results to the terminal
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${change_average}")
print(f"Greatest Increase in Profits: {max_inc_month} (${max_inc})")
print(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})")

#Export all of the results as a financial analysis text report
analysis = os.path.join('analysis','analysis.txt')
with open (analysis,'w') as text:
    text.write("Financial Analysis \n")
    text.write("--------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${change_average}\n")
    text.write(f"Greatest Increase in Profits: {max_inc_month} (${max_inc})\n")
    text.write(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})\n")