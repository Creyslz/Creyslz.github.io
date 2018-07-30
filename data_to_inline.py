import csv



titles = []
first = True
with open('ugh.txt', 'w') as outf:
  outf.write('[\n')
  with open('mydata.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      if first:
        titles = row
        first = False
        continue
      outf.write('  {\n')
      for i in range(len(row)):
        outf.write('    \"' + titles[i] + '\": \"' + row[i] + '\",\n')
      outf.write('  },\n')
  outf.write('];\n')