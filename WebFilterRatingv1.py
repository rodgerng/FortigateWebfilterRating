import sys
import csv
print("Copyright 2021 created by Rodger Ng Yong Fung")
set_rating = input("Enter Rating ID = ")
original_stdout = sys.stdout
# Save a reference to the original standard output

with open('output.txt', 'w') as f:
    sys.stdout = f
    # Change the standard output to the file we created.
    print("config webfilter ftgd-local-rating ")
    with open('blacklist.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(f'edit "{" ".join(row)}"')
            print("set rating " + set_rating)
            print("next")
            print("end")
            line_count += 1
    sys.stdout = original_stdout
# Reset the standard output to its original value
