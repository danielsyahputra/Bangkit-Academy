#!/usr/bin/env python3

# Importing modules
from asyncore import write
import re
import sys
import operator
import csv

def parse_log_file(logs):
    error_counter = {}
    per_user = {}

    for log in logs:
        error_log = re.search(r"ticky: ERROR ([\w ]*) .+ \((\w.+)\)", log)
        info_log = re.search(r"ticky: INFO ([\w ]*) .+ \((\w.+)\)", log)

        # Reporting log
        if error_log:
            error_message = error_log.group(1)
            username = error_log.group(2)
            if error_message not in error_counter:
                error_counter[error_message] = 1
            else:
                error_counter[error_message] += 1
            
            # User statistics
            if username not in per_user:
                per_user[username] = [0, 1]
            else:
                per_user[username][1] += 1
        if info_log:
            username = info_log.group(2)
            if username not in per_user:
                per_user[username] = [1, 0]
            else:
                per_user[username][0] += 1

    return error_counter, per_user

def sort_counter_and_per_user(error_counter, per_user):
    new_error_counter = sorted(error_counter.items(), key=operator.itemgetter(1), reverse=True)
    new_per_user = sorted(per_user.items(), key=operator.itemgetter(0))

    # Create headers for each counter
    new_error_counter.insert(0, ("Error", "Count"))
    new_per_user.insert(0, ("Username", ["INFO", "ERROR"]))
    return new_error_counter, new_per_user

def generate_csv(error_counter, per_user):
    # Generate error message report
    with open("error_message.csv", "w") as error_report:
        writer = csv.writer(error_report)
        for error, count in error_counter:
            writer.writerow([error, count])

    # Generate per user report
    with open("user_statistics.csv", "w") as user_report:
        writer = csv.writer(user_report)
        for username, count in per_user:
            writer.writerow([username, count[0], count[1]])

if __name__ == "__main__":
    log_file = open("syslog.log", "r")
    logs = log_file.readlines()
    error_counter, per_user =  parse_log_file(logs)
    error_counter, per_user = sort_counter_and_per_user(error_counter, per_user)
    generate_csv(error_counter, per_user)