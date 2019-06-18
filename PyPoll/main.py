#PyPoll
import os
import csv

votes = 0
candidates = []
khan = 0
otooley = 0
correy = 0
li = 0

path = 'election_data.csv'

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    
    for line in reader:
        votes += 1
        if line['Candidate'] == 'Khan':
            khan += 1
        if line['Candidate'] == "O'Tooley":
            otooley += 1
        if line['Candidate'] == "Correy":
            correy += 1
        if line['Candidate'] == "Li":
            li += 1
        candidates.append(line['Candidate'])


per_k = round((100*khan/votes), 2)
per_o = round((100*otooley/votes), 2)
per_c = round((100*correy/votes), 2)
per_l = round((100*li/votes), 2)

if khan > otooley and khan > correy and khan > li:
    winner = "Khan"
if otooley > khan and otooley > correy and otooley > li:
    winner = "O'Tooley"
if correy > khan and correy > otooley and correy > li:
    winner = "Correy"
if li > otooley and li > correy and li > khan:
    winner = "Li"


#OUTPUT
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes}")
print("----------------------------")
#print(set(candidates))
print(f"Khan: {per_k}% ({khan})")
print(f"O'Tooley: {per_o}% ({otooley})")
print(f"Correy: {per_c}% ({correy})")
print(f"Li: {per_l}% ({li})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

output_path = os.path.join("results.csv")

with open(output_path, 'w', newline='') as results:
    csvwriter = csv.writer(results, delimiter=',')
    
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {votes}"])
    csvwriter.writerow(["----------------------------"])    
    csvwriter.writerow([f"Khan: {per_k}% ({khan})"])
    csvwriter.writerow([f"O'Tooley: {per_o}% ({otooley})"])
    csvwriter.writerow([f"Correy: {per_c}% ({correy})"])
    csvwriter.writerow([f"Li: {per_l}% ({li})"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])

            