
import csv

file = '/users/krw252/ds/metis/metisgh/prework/dsp/python/faculty.csv'

def read_csv():
    faculty_data = []
    data = open(file ,'r')
    reader = csv.reader(data)
    for row in reader:
        faculty_data.append(row)
    data.close()
    return faculty_data

faculty = read_csv()

def get_dict():
    del faculty[0]
    names = []
    for row in faculty:
        name = row[0]
        last_name = name.rsplit()[0]
        names.append(last_name)
    info = []
    for row in faculty:
        del row[0]
        info.append(row)
    final = dict(zip(names,info))
    return (final)

print (get_dict())
