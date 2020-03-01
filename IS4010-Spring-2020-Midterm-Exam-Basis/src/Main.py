'''
Created on Feb 29, 2020
IS4010-Spring-2020-Midterm-Exam-Basis
@author: Bill Nicholson
nicholdw@ucmail.uc.edu
'''
from Utilities import *

mycsvdata = read_CSV_file("FL_insurance_sample.csv")     # Returns the data structure into mycsvdata
print(len(mycsvdata))
#print(mycsvdata[0])
counties = set([tmp[2] for tmp in mycsvdata])
print (sorted(counties))
print (len(counties)) 
count_in_pinellas = len([tmp[2] for tmp in mycsvdata if tmp[2].strip().lower() == "pinellas county"])
print(count_in_pinellas)
