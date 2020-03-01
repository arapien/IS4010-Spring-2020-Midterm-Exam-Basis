'''
Created on Feb 29, 2020
IS4010-Spring-2020-Midterm-Exam-Basis
@author: Bill Nicholson
nicholdw@ucmail.uc.edu
'''
import csv
def read_CSV_file(filename):
    csv_data = []
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
    #   csv_data.append(header)        # We don't want the header row.
        for row in reader:
            csv_data.append(row)
    
    #print(csv_data)
    #print (type(csv_data))      # It's a list of lists!
    return csv_data

