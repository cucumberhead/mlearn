import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import csv

with open('challenge_dataset.txt','r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped)
    with open("dat.csv","w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(("title","intro"))
        writer.writerows(lines)
