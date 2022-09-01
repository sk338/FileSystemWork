import os
import csv

all_files = [[img] for img in os.listdir('.\\images')]
print(all_files)

with open('ImageFiles.csv', 'w', newline='') as f:
    csvfile = csv.writer(f)
    csvfile.writerow(['image name'])
    csvfile.writerows(all_files)