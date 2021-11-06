
import time
import datetime
import calendar
import os
import math
import re
from exercise_0_lib import print_title

# Function

print_title('Function')

def sum(num_1, num_2):
	return (num_1 + num_2)

print('Sum of two numbers ' + str(sum(1, 3)))

# Exception

print_title('Exception')

try:
	num_so_big = 9999999999999999999999999999999999999999999999999

	raise ValueError('Number is so big exception')

	print('Number so big ' + str(num_so_big))
except ValueError as value_error:
	print(value_error)
else:
	print('Try except else')

try:
	num_so_big = 9999999999999999999999999999999999999999999999999

	# raise ValueError('Number is so big exception')

	print('Number so big ' + str(num_so_big))
except ValueError as value_error:
	print(value_error)
else:
	print('Try except else')

# Time

print_title('Time, Date Time, Calendar Module')

print(time.time())

print(datetime.datetime.now())

now_date = datetime.datetime.now()

print(datetime.datetime(now_date.year, now_date.month, now_date.day))

# OS

print_title('OS Module')

print(os.name)

try:
	os.mkdir('tmp_folder_created_by_python')
except:
	print('error to create tmp_folder_created_by_python')
else:
	print('created tmp_folder_created_by_python')

# Math

print_title('Math Module')

print('10 x 10 ' + str(math.pow(10, 2)))

num_pi = 3.142

print('Floor PI ' + str(math.floor(num_pi)))
print('Ceil PI ' + str(math.ceil(num_pi)))

# Reg Exp

print_title('Reg Exp')

email_valid = 'zmh@gmail.com'
email_invalid = 'zmh@'

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_email(email):
    if(re.match(email_regex, email)):
        print(email + ' is valid email')
    else:
        print(email + ' is invalid email')

check_email(email_valid)
check_email(email_invalid)

# File

print_title('File')

file_opened = open('misc/names.txt', 'r')

if file_opened:
	print('File opened')

file_read = file_opened.read()
print(file_read)

file_opened = open('misc/names.txt', 'w')

file_opened.write(file_read + '\n' + 'lorem ipsm')

file_opened.close()



































