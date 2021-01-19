import os
import csv
import operator

path = r"C:\Users\chamb\Desktop\python-challenge\PyPoll\Resources"
pypoll_csv = os.path.join(path,'election_data.csv')
file_to_save = os.path.join('analysis', 'analysis.txt')
results = {}
candidates=[]
khan = 0
otooley = 0
li = 0
correy = 0


with open(pypoll_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    total_votes = 0
    # Read each row of data after the header

    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])
    for x in candidates: 
        if (x == "Khan"): 
            khan = khan + 1
        if (x == "O'Tooley"):
            otooley = otooley + 1
        if (x == "Li"):
            li = li + 1
        if (x == "Correy"):
            correy = correy + 1
results = {"Khan":khan, "Correy":correy, "O'Tooley":otooley, "Li":li}

output = (
    f"Election Results\n"
    f"---------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------\n"
    f"Khan: {((khan/total_votes)*100):.3f}% ({khan})\n"
    f"Correy: {((correy/total_votes)*100):.3f}% ({correy})\n"
    f"Li: {((li/total_votes)*100):.3f}% ({li})\n"
    f"O'Tooley: {((otooley/total_votes)*100):.3f}% ({otooley})\n"
    f"Winner: {max(results.items(), key=operator.itemgetter(1))[0]}\n"
)

print(output)

#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary


with open(file_to_save, "w") as txt_file:
    txt_file.write(output)
