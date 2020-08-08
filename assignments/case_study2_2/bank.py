import csv 

with open('bank-data.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    input1 = input("enter job: ")
    for line in csv_reader:
        print(line['job'])
        
        

        

'''
    with open('new_details.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)
            print(line[1])
'''       


