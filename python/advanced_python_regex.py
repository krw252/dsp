#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:33:01 2017

@author: krw252
"""

import csv
import re

file = '/users/krw252/ds/metis/metisgh/prework/dsp/python/faculty.csv'

def dict_read_csv():
    faculty_data = []
    data = open(file ,'r')
    reader = csv.DictReader(data)
    for row in reader:
        faculty_data.append(row)
    data.close()
    return faculty_data

faculty = dict_read_csv()

def count_degrees(csv_file_name):
    degrees = ('MD', 'MA', 'SCD', 'BSED', 'PHD', '0', 'MPH', 'MS', 'JD')
    degree_dict = dict.fromkeys(degrees,0)
    MD = re.compile(r'm\.*d\.*', re.I)
    MA = re.compile(r'm\.*a\.*', re.I)
    SCD = re.compile(r's\.*c\.*d\.*', re.I)
    BSED = re.compile(r'b\.*s\.*e\.*d\.*', re.I)
    PHD = re.compile(r'p\.*h\.*d\.*', re.I)
    none = re.compile('0')
    MPH = re.compile(r'm\.*p\.*h\.*', re.I)
    MS = re.compile(r'm\.*s\.*', re.I)
    JD = re.compile(r'j\.*d\.*', re.I)
    for row in faculty:
        if MD.search(str(row[' degree'])):
            degree_dict['MD'] = degree_dict['MD'] + 1
    for row in faculty:
        if MA.search(str(row[' degree'])):
            degree_dict['MA'] = degree_dict['MA'] + 1
    for row in faculty:
        if SCD.search(str(row[' degree'])):
            degree_dict['SCD'] = degree_dict['SCD'] + 1
    for row in faculty:
        if BSED.search(str(row[' degree'])):
            degree_dict['BSED'] = degree_dict['BSED'] + 1
    for row in faculty:
        if PHD.search(str(row[' degree'])):
            degree_dict['PHD'] = degree_dict['PHD'] + 1
    for row in faculty:
        if none.search(str(row[' degree'])):
            degree_dict['0'] = degree_dict['0'] + 1
    for row in faculty:
        if MPH.search(str(row[' degree'])):
            degree_dict['MPH'] = degree_dict['MPH'] + 1
    for row in faculty:
        if MS.search(str(row[' degree'])):
            degree_dict['MS'] = degree_dict['MS'] + 1
    for row in faculty:
        if JD.search(str(row[' degree'])):
            degree_dict['JD'] = degree_dict['JD'] + 1
    return (degree_dict)

def count_titles(csv_file_name):
    titles = []
    for row in faculty:
        titles.append(row[' title'])
    titles_dict = dict.fromkeys(titles,0)
    for row in faculty:
        if re.match('Associate' ,str(row[' title'])):
            titles_dict['Associate Professor of Biostatistics'] = titles_dict['Associate Professor of Biostatistics'] + 1
    for row in faculty:
        if re.match('Professor' ,str(row[' title'])):
            titles_dict['Professor of Biostatistics'] = titles_dict['Professor of Biostatistics'] + 1
    for row in faculty:
        if re.match('Assistant' ,str(row[' title'])):
            titles_dict['Assistant Professor of Biostatistics'] = titles_dict['Assistant Professor of Biostatistics'] + 1
    return (titles_dict)

def emails(data):
    emails = []
    for row in data:
        emails.append(row[' email'])
    return (emails)

def domains(email_list):
    domains = []
    for e in email_list:
        d = e.split('@')
        domains.append(d[1])
    return (set(domains))

def read_csv():
    faculty_data = []
    data = open(file ,'r')
    reader = csv.reader(data)
    for row in reader:
        faculty_data.append(row)
    data.close()
    return faculty_data

faculty_b = read_csv()

def get_dict():
    del faculty_b[0]
    names = []
    for row in faculty_b:
        name = row[0]
        last_name = name.rsplit()[0]
        names.append(last_name)
    info = []
    for row in faculty_b:
        del row[0]
        info.append(row)
    final = dict(zip(names,info))
    return (final)

print(count_degrees(faculty))
print(count_titles(faculty))
print(emails(faculty))
print (domains(emails(faculty)))
print (get_dict())
