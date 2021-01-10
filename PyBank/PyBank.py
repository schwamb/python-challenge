#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
import os
import csv
import operator

pybank_csv = os.path.join('Resources', 'budget_data.csv')
months = []
profit_losses = []
bank_data = {}
average_change = []
ac = float()
currentrow=int()
nextrow = int()

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
    
    # for row in profit_losses:    
    #     currentrow=(profit_losses[0])
    #     nextrow=(profit_losses.index[0]
        #ac=(nextrow-currentrow)
        #average_change.append(ac)

    #print(profit_losses.index(1))
   # print((average_change))
    #print(ac)
   #print(nextrow)
    #print(currentrow)
#     print(profit_losses)


    for month in months:
        for value in profit_losses:
            bank_data[month] = value
            profit_losses.remove(value) 
            break  

    # for row in csvreader:
    #     profit_losses.append(int(row[1]))


    average = (sum(average_change)/(len(months)-1))
    maximum = round(max(bank_data.values()),2)
    minimum = round(min(bank_data.values()),2)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(months)}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {list(bank_data.keys())[list(bank_data.values()).index(maximum)]} (${maximum})')
    print(f'Greatest Decrease in Profits: {list(bank_data.keys())[list(bank_data.values()).index(minimum)]} (${minimum})')

  #Average change is meant to be the average of the change from month to month
  # subtract rox[1] index i+1 from index i
  # store these values
  # average these vaues