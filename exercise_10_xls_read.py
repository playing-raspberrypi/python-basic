
import xlrd

xlrd_opened_workbook = xlrd.open_workbook('misc/excel_file_1.xls')
xlrd_opened_workbook_sheet = xlrd_opened_workbook.sheet_by_index(0)
xlrd_opened_workbook_sheet_2 = xlrd_opened_workbook.sheet_by_index(1)

for i in range(xlrd_opened_workbook_sheet.nrows):
    print(xlrd_opened_workbook_sheet.cell_value(i, 0))

print()

for i in range(xlrd_opened_workbook_sheet.ncols):
    print(xlrd_opened_workbook_sheet.cell_value(0, i))

print()

for i in range(xlrd_opened_workbook_sheet_2.nrows):
    print(xlrd_opened_workbook_sheet_2.cell_value(i, 0))

print()

print(f'Total rows {xlrd_opened_workbook_sheet.nrows}')
print(f'Total cols {xlrd_opened_workbook_sheet.ncols}')