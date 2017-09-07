import csv
import re

facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

with open('faculty.csv', 'w') as f:
    f.write(facultycsv)

def read_csv():
    faculty_data = []
    data = open('faculty.csv','r')
    reader = csv.DictReader(data)
    for row in reader:
        faculty_data.append(row)
    data.close()
    return faculty_data

faculty = read_csv()

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

print(count_degrees(faculty))
