"""
Q1 >> p a
    Create two csv files named stud1.csv (rollno,name,place,category) to contain data like,
    101, Tom, Calicut, SCST
    102, Raj, Kanur, General

    and mark1.csv (rollno,sub, mark) to contain data like,
    101, sci, 76
    101, mat, 88
    101, eng, 90
    102, sci, 76

    Populate the files with a minimum of 5 and 15 records respectively.
    Write a script to name and total marks for each candidate
>>
"""
master_records = ["101, Tom, Calicut, General",
                  "102, Raj, Kanur, General",
                  "103, Rohit, Trivandrum, SCST",
                  "104, Rahul, Ernakulam, OBC",
                  "105, Remya, Kollam, General"]

marks = ["101, sci, 76",
         "101, mat, 88",
         "101, eng, 90",
         "102, sci, 78",
         "102, mat, 78",
         "102, eng, 87",
         "103, sci, 69",
         "103, mat, 73",
         "103, eng, 89",
         "104, sci, 79",
         "104, mat, 75",
         "104, eng, 82",
         "105, sci, 81",
         "105, mat, 69",
         "105, eng, 71"
         ]

with open("stud1.csv", "w") as file:
    file.write("rollno, name, place, category\n")
    for line in master_records:
        file.writelines(line)
        file.write("\n")

with open("mark1.csv","w") as file:
    file.write("rollno, sub, mark\n")
    for line in marks:
        file.writelines(line)
        file.write("\n")

import pandas as pd
f1 = pd.read_csv("stud1.csv")
#print f1
f2 = pd.read_csv("mark1.csv")
#print f2
f3 = pd.merge(f1,f2, on="rollno")
print f3
f4 = f3.set_index(['rollno',' name'])
print (f4)
print f4.sum(level=' name')[' mark']
print f4.sum(level='rollno')[' mark']


"""
Q2 >> pybdatest C

Store yarn.default.xml to your directory and write a script to parse values of 'name' and 'value' tags into a panda 
dataframe. Display the dataframe.
"""
import xml.etree.ElementTree as et

xtree = et.parse("yarn.default.xml")
xroot = xtree.getroot()
df_cols = ["Name","Value"]
df = pd.DataFrame(columns=df_cols)

for node in xroot:
    s_name = node.find("name").text
    s_value = node.find("value")
    if s_value is not None:
        s_value = s_value.text
    else:
        s_value = None

    df = df.append(pd.Series([s_name,s_value], index=df_cols),ignore_index=True)

print df
""" Q3 >> pybdatest D
Write a python script to print the count of (top 10) words in a given file and plot the words against the counts
"""

from collections import Counter
words_dict = dict()
with open("story.txt") as file:
    for line in file.readlines():
        words = line.split()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

print words_dict

word_counter = Counter(words_dict)
lst = word_counter.most_common(10)
print 'type', type(lst)
df = pd.DataFrame(lst, columns=['Words', 'Counts'])
print df
df.plot.bar(x='Words',y='Counts')

""" Q3 >> pybdatest A
    Create two csv files named stud1.csv (rollno,name,place,category) to contain data like,
    101, Tom, Calicut, SCST
    102, Raj, Kanur, General

    and mark1.csv (rollno,sub, mark) to contain data like,
    101, sci, 76
    101, mat, 88
    101, eng, 90
    102, sci, 76

    Populate the files with a minimum of 5 and 15 records respectively.
    Write a script to print name with place in brackets (both in upper case) and rank for each candidate.
"""

f3 = pd.read_csv("stud1.csv")
f4 = pd.read_csv("mark1.csv")
f5 = pd.merge(f3,f4, on="rollno")
print f5
f6 = f5.set_index(['rollno',' name'])
print f6
print f6.rank()



""" Q4 pybdatest B
Write a script to draw a plot to analyse the size of files in any given directory. File names should be present in 
plot as xticks lables.
Syntax for running script: $ script <dirname>
"""
import os, sys
import matplotlib.pyplot  as plt
start_path = None
try:
    if sys.argv[1]:
        start_path = sys.argv[1]
    else:
        start_path = '.'
except IndexError:
    start_path = '.'


files_counts = {}
for dirpath, dirnames, filenames in os.walk(start_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        try:
            stat = os.stat(fp)
        except OSError:
            continue
        #fileName  = dirpath.join(f)
        if f not in files_counts:
            files_counts[f] = stat.st_size
print files_counts
df = pd.DataFrame()
df['File Name'] = files_counts.keys()
df['Counts'] = files_counts.values()
print df
#df.plot.bar(x="File Name",y="Counts")
#plt.bar(files_counts.keys(),files_counts.values())
#plt.xticks(files_counts.keys())
#plt.ylabel("File Size in MB")
#plt.show()

"""Q5 p c
Take a copy of book.xml to your eaxm directory and write a script to parse it to store values of 'title' and 'price' 
tags into a dataframe. Display the dataframe.
"""
xtree = et.parse("book.xml")
xroot = xtree.getroot()

df_cols = ["category", "title", "author", "year", "price"]
#df = pd.DataFrame(columns=df_cols)
df = pd.DataFrame(columns=["year", "price"])

for node in xroot:
    s_category = node.attrib.get("category")
    s_title = node.find("title").text
    s_author = node.find("author").text
    s_year = node.find("year").text
    s_price = node.find("price").text
    #df = df.append(pd.Series([s_category,s_title,s_author,s_year,s_price],index=df_cols), ignore_index=True)

    df = df.append(pd.Series([s_year, s_price], index=["year", "price"]), ignore_index=True)

print df
