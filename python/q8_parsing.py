# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

file = '/Users/krw252/ds/metis/metisgh/prework/dsp/python/football.csv'

def read_csv():
    football_data = []
    f = open(file,'r')
    reader = csv.DictReader(f)
    for row in reader:
        football_data.append(row)
    f.close()
    return football_data

football_data = read_csv()

def lowest_goal_diff(dict):
    diff = 0
    team = ''
    for d in range(0,len(dict)):
        if int(dict[d]['Goals']) - int(dict[d]['Goals Allowed']) < diff:
            diff = int(dict[d]['Goals']) - int(dict[d]['Goals Allowed'])
            team = dict[d]['Team']
    return 'Team with the lowest goal differential was %s with a differential of %d.' % (team,diff)

print (lowest_goal_diff(football_data))
#Team with the lowest goal differential was Leicester with a differential of -34.
