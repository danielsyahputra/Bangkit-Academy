#!/usr/bin/env python3

import os
import datetime
import reports_2
import emails_2

DIR = "{}/supplier-data/descriptions".format(os.getenv('HOME'))
DEST = "/tmp/processed.pdf"

files = os.listdir(DIR)

def main():

    # Set content
    content = []
    for file in files:
        with open(os.path.join(DIR, file), 'r') as f:
            lines = [line.replace('\n',"") for line in f]
            name = "name: {}".format(lines[0])
            weight = "weight: {}".format(lines[1])
            paragraph = "{}<br>{}<br>".format(name, weight)
            content.append(paragraph)
    content = "<br>".join(content)

    # Set title
    today = datetime.datetime.today()
    today = today.strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)

    # Report
    reports_2.generate_report(filename=DEST, title=title, content=content)

    # Send email
    message = emails_2.generate_email(
        "automation@example.com", 
        "{}@example.com".format(os.getenv("USER")),
        "Upload Completed - Online Fruit Store",
        "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        DEST
    )
    emails_2.send(message)

if __name__=="__main__":
    main()