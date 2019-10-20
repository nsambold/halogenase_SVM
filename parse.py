import csv

dic = {}
keylst = []

with open('blosum64.csv', newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    keylst = next(reader)
    for key, val in zip(keylst, reader):
        dic[key] = [int(val) for val in val[1:]]

with open("converter.py", "w") as f:
    f.write("dic = {\n")
    for key, val in dic.items():
        f.write("\t" + "\'" + key + "\'" + ": " + str(val) + "," + "\n")
    f.write ("}")
