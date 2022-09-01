# Split the CSV file into number of copies as per user's choice

import os
import math

SPLIT_RECORD_COUNT = 2000
CSV_FILE_NAME = 'AddressOutput.csv'

with open(f'.\\{CSV_FILE_NAME}', 'r') as f:
    csvfile = f.readlines()

# print(len(csvfile))

if not os.path.exists('.\\CSV'):
    os.mkdir('.\\CSV')

counter = 1

# print(math.ceil(len(csvfile)/SPLIT_RECORD_COUNT))
# frac, whole = math.modf(len(csvfile)/SPLIT_RECORD_COUNT)
# print(frac, whole)
# if frac > 0:
#     # endRange = (math.ceil(len(csvfile)/SPLIT_RECORD_COUNT))
#     endRange = int(len(csvfile)/SPLIT_RECORD_COUNT)
#     print(endRange)
# else:
#     # endRange = (math.ceil(len(csvfile)/SPLIT_RECORD_COUNT))
#     endRange = int(len(csvfile)/SPLIT_RECORD_COUNT)
#     print(endRange)

endRange = (math.ceil(len(csvfile)/SPLIT_RECORD_COUNT)+1)

for i in range(1, endRange):
    start = i + counter - 1
    end = i * SPLIT_RECORD_COUNT + 1
    # print(start, end)
    with open(f'.\\CSV\\{i}_{CSV_FILE_NAME}', 'w') as f:
        f.write('filename,address,city,state,zipcode,map_year,image_captured_date,image_type,link\n')
        for row in csvfile[start:end]:
            f.write(row)

    counter += (SPLIT_RECORD_COUNT-1)
    print(f'Done record: {i}')

