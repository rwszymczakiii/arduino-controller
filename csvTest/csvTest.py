import csv
with open('./csvTest/test.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['hey'])
    spamwriter.writerow(['hey'])