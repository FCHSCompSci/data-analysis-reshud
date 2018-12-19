import csv

filename = 'corruption'
with open(filename) as f:
 reader = csv.reader(f)
 header_row = next(reader)
 print(header_row)

 snip
with open(filename) as f:
 reader = csv.reader(f0
 header_row = next(reader)

 for index, column_header in enumerate(header_row):


rank , highs = [], []
 for row in reader:
     current_rank = rank(row[0], "max_range")
     rank.append(max_range)


#plot data
fig = plt.figure(dpi=128)
plt.plot(highs, c='red')

#foramt plot.
plt.tittle("corruption perception index, 2016",)

