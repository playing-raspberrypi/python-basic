
import csv

csv_field_1 = 'First Name'
csv_field_2 = 'Last Name'
csv_field_3 = 'Rank'

with open('misc/tmp_csv_created_by_python.csv', 'w') as csv_file:
    csv_fields = [csv_field_1, csv_field_2, csv_field_3]
    writer = csv.DictWriter(csv_file, fieldnames = csv_fields)

    writer.writeheader()
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Zaw Moe', csv_field_2: 'Htike'})
    writer.writerow({csv_field_3: 'A', csv_field_1: 'Smith', csv_field_2: 'Rodriguez'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Oscar'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Loive'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Zaw Moe', csv_field_2: 'Htike'})
    writer.writerow({csv_field_3: 'A', csv_field_1: 'Smith', csv_field_2: 'Rodriguez'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Oscar'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Loive'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Zaw Moe', csv_field_2: 'Htike'})
    writer.writerow({csv_field_3: 'A', csv_field_1: 'Smith', csv_field_2: 'Rodriguez'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Oscar'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Loive'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Zaw Moe', csv_field_2: 'Htike'})
    writer.writerow({csv_field_3: 'A', csv_field_1: 'Smith', csv_field_2: 'Rodriguez'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Oscar'})
    writer.writerow({csv_field_3: 'B', csv_field_1: 'Jane', csv_field_2: 'Loive'})

print("Writing complete")






































