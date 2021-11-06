import csv

line_count = 0

def print_table_records(row):
    print(
        '\t'
        + row['Name'] + ' | '
        + row['Hire Date'] + ' | '
        + row['Salary'] + ' | '
        + row['Leaves Remaining']
    )
    print(row)

def print_table_attributes(row):
    print(
        '\t'
        + ' | '.join(row)
    )
    print(row)

with open('misc/employee.csv', mode='r') as opened_file:
    csv_dict_reader = csv.DictReader(opened_file)
    for row in csv_dict_reader:
        if line_count == 0:
            print_table_attributes(row)
            line_count += 1
            
        print_table_records(row)
        line_count += 1

print(f'\t******Processed record {line_count - 1} lines.')































