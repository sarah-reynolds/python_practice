# Lists are changeable. Tuples can not be changed.

a_tuple = (1,3,8)
# print a_tuple
# print a_tuple[2]

# loop through tuples the same way you do wth lists
# for number in a_tuple:
# 	print number

# teams = ('falcons','hawks','atl_united','silverbacks')
# for team in teams:
# 	if team == 'hawks':
# 		print 'go hawks'
# 	else:
# 		print "it's basketball season"

# team_b = 'braves'
# cond1 = (team_a == 'falcons')
# cond2 = (team_b == 'braves')
# if cond1 and cond2:
# 	print 'hooray'

# print 'hawks' in teams

# for team in teams:
# 	if team == 'hawks':
# 		print 'go hawks'
# 	elif team == 'falcons':
# 		print 'sad superbowl'

# if 'hawks' in teams:
# 	print 'go hawks'
# elif 'falcons' in teams:
# 	print 'go falcons'

# height = raw_input('Enter your height in inches\n')
# if(int(height) >= 42):
# 	print "You are tall enough to go on the Batman roller coaster"
# else:
# 	print "Maybe try the kiddie coaster."

current = 1
# while (current < 10):
# 	print current
# 	current+=1

answer = 'play'
while answer != 'quit':
	answer = raw_input('say quit to stop the game\n')

