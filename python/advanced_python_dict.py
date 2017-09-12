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
    names = []
    for row in faculty[1:]:
        name = row[0]
        last_name = name.rsplit()[0]
        names.append(last_name)
    info = []
    for row in faculty[1:]:
        info.append(row[1:])
    final = dict(zip(names,info))
    return (final)

def professor_dict():
    names = []
    for row in faculty[1:]:
        name = row[0]
        last_name = (name.rsplit()[0], name.rsplit()[-1])
        names.append(last_name)
    info = []
    for row in faculty[1:]:
        info.append(row[1:])
    final = OrderedDict(zip(names,info))
    return (final)

#why does this function sort by second element of key?
def last_name():
    a = professor_dict()
    for (f,l), v in a.items():
        print ("%s: %s" % ((l,f), v))

last_name()
print('\n', list(faculty_dict().items())[:3], '\n\n', list(professor_dict().items())[:3])
