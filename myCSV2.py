import csv

with open('myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
#    prices = []
    for row in readCSV:
        color = row[3]
        date = row[0]
#        price = row[4]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
