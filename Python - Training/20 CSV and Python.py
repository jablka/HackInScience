import csv
import datetime

def generate_csv(a_list):

    container = []
    for riadok in a_list:
        mydict = { i[0]:i[1] for i in riadok }
        # print(mydict)
        mydict['date'] = mydict['date'].strftime("%m/%d/%Y") # date
        mydict['locations'] = ",".join(mydict['locations'])
        container.append(mydict)    

    # writing to CSV
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = [ i for i in container[0] ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in container:
            writer.writerow(i)
        
        
def parse_csv():
    with open('students.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        result = []
        for row in reader:
            
            # print(row['Birthdate'])
            my_date = datetime.datetime.strptime(row['Birthdate'], '%m/%d/%Y' )
            my_string = f'{my_date.year},{my_date.month},{my_date.day}' 
            row['Birthdate']=eval('datetime.date('+my_string+')')
            
            # print(row['Marks'])
            row['Marks']= [ int(i) for i in row['Marks'].split(',') ] 
            
            # print(row)
            # print()

            result.append(row)
    
    return result
