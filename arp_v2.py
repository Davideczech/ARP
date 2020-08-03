import csv

arptable = {}
mactable = {}

#ARP table parsing - crating dict "arptable" mac-ip mapping
with open('ARP_test.txt', 'r') as f:

    for line in f:
        cols = line.split() #split line at whitespace
        try:
            if cols[-3].strip() in arptable.keys():
                arptable.setdefault(cols[-3].strip(),[]).append(cols[-5].strip())
            else:
                arptable[cols[-3].strip()] = [cols [-5].strip()]
        except IndexError:
            pass

with open('MAC_test.txt', 'r') as e:

    for line in e:
        cols = line.split() #split line at whitespace
        try:
            if cols[-1].strip() in mactable.keys() and cols[-6].strip() in arptable.keys():
                mactable.setdefault(cols[-1].strip(),[]).append(arptable[cols[-6]])
            elif cols[-6].strip() in arptable.keys():
                mactable[cols[-1].strip()] = [arptable[cols[-6].strip()]]
        except IndexError:
            pass
#Merging lists in the dictionary values
for key in mactable:
    new_list = []
    for value in mactable[key]:
        new_list += value
    mactable[key] = new_list

#Removing duplicates from the dictionary items
result = {a:list(set(b)) for a, b in mactable.items()}

#Generating csv file with the results
with open('ARP_result.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in result.items():
            writer.writerow([key, value])