import os
import sys

import csv

with open("./training_environment.yml") as inp:
    reader = csv.reader(inp)
    for record in reader:
        print(record)