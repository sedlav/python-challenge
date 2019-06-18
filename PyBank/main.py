#PyBank
import os
import csv

months = 0
total = 0
avg = 0
max_inc = 0
min_dec = 0

path = 'budget_data.csv'

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    
    for line in reader:
        #print(line['Profit/Losses'])
        months += 1
        total += int(line['Profit/Losses'])
        
#        if int(line['Profit/Losses']) > max_inc:
#            max_inc = line

#print(max_inc)
        
        
avg = round((total/months), 2)


#OUTPUT
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits:")
print(f"Greatest Decrease in Profits:")

output_path = os.path.join("results.csv")

with open(output_path, 'w', newline='') as results:
    csvwriter = csv.writer(results, delimiter=',')
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {months}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change: ${avg}"])
    csvwriter.writerow([f"Greatest Increase in Profits:"])
    csvwriter.writerow([f"Greatest Decrease in Profits:"])

    
