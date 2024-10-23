# This code is written by ChatGPT 
# I didn't write this code.
import csv

# Open the TXT file and read its contents
with open('data_raw.txt', 'r') as txt_file:
    lines = txt_file.readlines()

# Write the contents to a CSV file
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Assuming the TXT file uses spaces as a delimiter
    for line in lines:
        # Split the line into a list
        row = line.strip().split()  # Change split() to split(',') if using commas
        writer.writerow(row)