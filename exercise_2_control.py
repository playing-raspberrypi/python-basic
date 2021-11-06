
from exercise_0_lib import print_title

# Conditons

print_title('Conditions')

num_1 = 10
num_2 = 20

if(num_1 < num_2):
	print('num_1 is less than num_2')

if(num_1 != num_2):
	print('num_1 and num_2 are not equal')

if(num_1 <= num_2):
	print('num_1 is less than or equal num_2')

# Loop

print_title('Loop')

friends = ['Obama', 'Robert Kiosaki', 'Stephen Hawkin']
tmp_friends = []

for friend in friends:
	tmp_friends += [friend]

print(tmp_friends)

tmp_friends_2 = []

for i in range(len(friends)):
	tmp_friends_2 += [friends[i]]

print(tmp_friends_2)

# While Loop

print_title('While Loop')

start_point = 0
tmp_friends_3 = []

while start_point < len(friends):
	tmp_friends_3 += [friends[start_point]]
	start_point = start_point + 1

print(tmp_friends_3)








































