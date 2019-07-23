import csv

with open('test.csv', 'r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        for row in reader:
            row.append('new string') 
            row.append('new string 2')
            all.append(row) 
            
        writer.writerows(all)
