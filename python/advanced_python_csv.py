import csv

file = '/users/krw252/ds/metis/metisgh/prework/dsp/python/faculty.csv'

def read_csv():
    faculty_data = []
    data = open(file ,'r')
    reader = csv.DictReader(data)
    for row in reader:
        faculty_data.append(row)
    data.close()
    return faculty_data

faculty = read_csv()

def emails(data):
    emails = []
    for row in data:
        emails.append(row[' email'])
    return (emails)
  
  def write_to_csv(list_of_emails):
    path = '/users/krw252/ds/metis/metisgh/prework/dsp/python/emails.csv'
    result_file = open(path, 'w')
    result_file.write('list of emails' + '\n')
    for r in list_of_emails:
        result_file.write(r + '\n')
    result_file.close()

write_to_csv(emails(faculty))
