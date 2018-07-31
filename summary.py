import csv

csvFileReader = open("C:\\Users\Administrator\Documents\data.csv", "r")
reader = csv.reader(csvFileReader)

i = 0


csvFileWriter = open("pro.csv", "w", newline='')
writer = csv.writer(csvFileWriter)
#fileHeader = ["name", "score"]

minProb = 0

for item in reader:

    if minProb > float(item[1]):
        minProb = float(item[1])

    i = (i+1) % 48

    if i == 0:
        writer.writerow([str(minProb)])
        minProb = 1

