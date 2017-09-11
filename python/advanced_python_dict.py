
import csv
from collections import OrderedDict

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

def faculty_dict():
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

print(list(faculty_dict().items())[:3])

def professor_dict():
    del faculty[0]
    names = []
    for row in faculty:
        name = row[0]
        last_name = (name.rsplit()[0], name.rsplit()[-1])
        names.append(last_name)
    info = []
    for row in faculty:
        del row[0]
        info.append(row)
    final = OrderedDict(zip(names,info))
    return (final)

print(list(professor_dict().items())[:3])
