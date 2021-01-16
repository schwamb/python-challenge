import os
import csv
import operator

path = r"C:\Users\chamb\Desktop\python-challenge\PyPoll\Resources"
pypoll_csv = os.path.join(path,'election_data.csv')
results = {}

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

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
        results = {"Candidate" : }
        profit_losses.append(int(row[1]))
        

print(f"Total Votes: {total_votes} Khan Votes: {khan_votes}")
        

# candidate votes percent and Raw
# winner
#         * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
