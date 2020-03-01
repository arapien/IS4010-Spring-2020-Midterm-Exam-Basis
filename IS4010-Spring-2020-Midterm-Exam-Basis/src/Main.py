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
# Print the first and last counties in alphapetical order
counties = set([tmp[2] for tmp in mycsvdata])
print (sorted(counties)[0], sorted(counties)[-1])
# print the total number of counties
print (len(counties)) 
# print the number of entries (rows) in Pinellas County
count_in_pinellas = len([tmp[2] for tmp in mycsvdata if tmp[2].strip().lower() == "pinellas county"])
print(count_in_pinellas)
# print the policy number of the property at latitude 26.6534  and longitude  -80.208191
policy_number = [tmp[0] for tmp in mycsvdata if tmp[13].strip().lower() == "26.6534" and tmp[14].strip().lower() == "-80.208191"]
print(policy_number)

