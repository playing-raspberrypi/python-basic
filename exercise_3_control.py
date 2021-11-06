
from exercise_0_lib import print_title

friends = ['Lincoln', 'Washington', 'Obama', 'Bush', 'Truman', 'Roosevelt']
tmp_friends = []

print(friends)
print(tmp_friends)

# Break

print_title('Break')

friend_counter = 0

for friend in friends:
	friend_counter += 1
	if(friend_counter > 3):
		break

	tmp_friends += [friend]

print(tmp_friends)

tmp_friends = []

# Continue

print_title('Continue')

friend_counter = 0

for friend in friends:
	friend_counter += 1
	if(friend_counter == 3):
		continue

	tmp_friends += [friend]

print(tmp_friends)

tmp_friends = []
































