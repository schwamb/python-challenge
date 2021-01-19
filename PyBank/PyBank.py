import os
import csv
import operator

pybank_csv = os.path.join('Resources', 'budget_data.csv')
file_to_save = os.path.join('analysis', 'analysis.txt')

months = []
profit_losses = []
difference = []
with open(pybank_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    
    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

    
    net_total = round(sum(profit_losses),2)

    i = 0
    j = 0
    for row in profit_losses:
        if i < (len(list(profit_losses))-1):
            month1 = (profit_losses[j])
            i += 1
            month2 = (profit_losses[i])
            difference.append(month2-month1)

            j +=1
    
    average = (sum(difference)/(len(months)-1))
    maxdiff = round(max(difference))
    mindiff = round(min(difference))
    maxloc = difference.index(maxdiff)+1
    minloc = difference.index(mindiff)+1


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f'Total Months: {len(months)}\n'
    f'Total: ${net_total}\n'
    f'Average Change: ${average:.2f}\n'
    f'Greatest Increase in Profits: {months[maxloc]} (${maxdiff})\n'
    f'Greatest Decrease in Profits: {months[minloc]} (${mindiff})\n'
)

print(output)

with open(file_to_save, "w") as txt_file:
    txt_file.write(output)



