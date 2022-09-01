# Move the images based on CSV file into separate folders

import os
import shutil

IMAGE_FOLDER_NAME = 'images'

i = 1
# counter = 1

allCSVFiles = os.listdir('.\\CSV')

for m, imageFile in enumerate(allCSVFiles):
    with open(f'.\\CSV\\{imageFile}', 'r') as f:
        csvfile = f.read().split('\n')

    all_files = os.listdir(f'.\\{IMAGE_FOLDER_NAME}')

    # if counter > i * 5:
    #     i += 1

    for fil in csvfile:
        for img in all_files:
            if img == fil.split(',')[0]:
                if not os.path.exists(f'.\\{IMAGE_FOLDER_NAME}{i}'):
                    os.mkdir(f'.\\{IMAGE_FOLDER_NAME}{i}')
                shutil.move(f'.\\{IMAGE_FOLDER_NAME}\\{img}', f'.\\{IMAGE_FOLDER_NAME}{i}')

                # counter += 1
    i += 1
    print(f'Done file: {imageFile}')