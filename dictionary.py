zombie = {
	'speed': 10,
	'power': 6,
	'hunger': 12,
	'name': 'Zombie'
}

# print zombie['speed']
zombie['weapon'] = 'fist'
zombie['startx'] = 200
zombie['starty'] = 100
# print zombie

if zombie['speed'] < 5:
	zombie['position'] = zombie['startx'] + 2
elif zombie['speed'] < 10:
	zombie['position'] = zombie['startx'] + 4
else:
	zombie['position'] = zombie['startx'] + 6

zombie['pointless'] = 'duh'
# print zombie
del zombie['pointless']
# print zombie

skill1= 'redux'
techs = {
	'html': 10,
	'css': 8,
	'javascript': 7,
	'react': 7,
	'mysql': 5,
	'node': 4,
	skill1: 3
}

# print techs

# for key,value in techs.items():
# 	print value

# if zombie.has_key('mother_name'):
# 	print zombie['mother_name']

# if techs.has_key('html'):
# 	print techs['html']

# for key in zombie:
# 	print zombie[key]

zombies = []
zombies.append({
	'speed': 10,
	'power': 6,
	'hunger': 5,
	'name': 'Bill'
	})

zombies.append({
	'speed': 5,
	'power': 16,
	'hunger': 9,
	'name': 'Sven'
	})

# print zombies
# print zombies[0]['name']

# for zombie in zombies:
# 	print zombie['name']

zombies[0]['victims'] = ['Sean','Rishi','Anna']
# print zombies[0]

# zombies[0]['victims'][0]['name'] = 'Sean'
# print zombies[0]

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# print phonebook_dict['Elizabeth']
# phonebook_dict['Kareem'] = '938-489-1234'
# print phonebook_dict
# del phonebook_dict['Alice']
# print phonebook_dict
# phonebook_dict['Bob'] = '968-345-2345'
# print phonebook_dict
# for key,value in phonebook_dict.items():
# 	print value

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# print ramit['email']
# print ramit['interests'][0]
# print ramit['friends'][0]['email']
# print ramit['friends'][1]['interests'][1]


# letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}

def letter_histogram(string):
	letter_counter = {}
	counter = 0
	for letter in string:
		if letter in letter_counter:
			letter_counter[letter]+=1
		else:
			letter_counter[letter]=1
	print letter_counter

letter_histogram('banana')
