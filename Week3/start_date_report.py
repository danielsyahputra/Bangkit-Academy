#!/usr/bin/env python3

import csv
import datetime
from mailbox import linesep
import operator
from urllib import response
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer():
    pass

def get_dict_employees_date(reader, start_date):
    employees = {}
    for row in reader:
        current_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if current_date < start_date:
            continue
        if row[3] not in employees:
            employees[row[3]] = []
        employees[row[3]].append("{} {}".format(row[0], row[1]))
    
    return employees

def list_newer(start_date):
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    reader = sorted(reader, key=operator.itemgetter(3), reverse=False)
    employees = get_dict_employees_date(reader, start_date)
    for date, employee in employees.items():
        date_format = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d, %Y")
        print("Started on {}: {}".format(date_format, employee))

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__=="__main__":
    main()