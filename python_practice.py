string = "Cheese"
# print string.upper()
# print string.title()
# print string[::-1]


# replacements = (('A','4'), ('E','3'), ('G','6'), ('I','1'), ('O','0'), ('S','5'), ('T','7'))
# new_string = string.upper()
# for old, new in replacements:
# 	new_string = new_string.replace(old, new)

# print new_string


# ****************************************

## example of a list containing lists
# list_example = [
#    ['puppy','dog'], 
#    ['kitten','cat'], 
#    ['cub','bear'], 
#    ['calf','cow'], 
#    ['chick','chicken'], 
#    ['fawn','deer']
# ]

# print list_example[0]   ## this will print the first item in the list, which is ['puppy','dog']
# print list_example[0][0]   ## this will print the first item of the first item in the list, which is 'puppy' 
# print list_example[0][1]   ## this will print the SECOND item of the first item in the list, which is 'dog' 

# ****************************************

# from string import maketrans
# intab = "AEGIOST"
# outtab = "4361057"
# trantab = maketrans(intab,outtab)
# print string.upper().translate(trantab)

# vowel_replace = (('aa','aaaaa'),('ee','eeeee'),('ii','iiiii'),('oo','ooooo'),('uu','uuuuu'))
# vow_string = string.lower()
# for old, new in vowel_replace:
# 	vow_string = vow_string.replace(old,new)
# print (vow_string)




####################################
####################################
####################################


# String Excercises
# string_as_a_string = "This is a string"


# # --Leetspeak
# characters_to_be_replaced = ["A","E","G","I","O","S","T"]
# Characters_to_replace_with = ["4","3","6","1","0","5","7"]
# character_replacement_list = []

# for character in string_as_a_string.upper():
#     print character
#     print characters_to_be_replaced.index(character)
   #  for replaceable in characters_to_be_replaced:
   #      # print replaceable
   # # print string_as_a_string.upper()
   # # print (character)
   # # print (replaceable)
   #      if character == replaceable:
   #          # print "character is replaceable"
   #          character_replacement_list.append("x")

   #   # print (character)
   #   # print Characters_to_replace_with.index(replaceable)
   #          # print Characters_to_replace_with.index(character)
   #   # character_replacement_list.append(Characters_to_replace_with.index(replaceable))
   #      else:
   #   # print (character)
   #          character_replacement_list.append(character)
# print (character_replacement_list)
 # if character == characters_to_be_replaced[i]:
# print character_replacement_list

####################################
####################################
####################################



# print vow_string

# for i in range(1,11):
# 	print i

# size = 5
# for i in range(size):
# 	print('*'*size)


# hollow square with user input
# print "how wide do you want the hollow square?"
# height = int(raw_input())
# print "how tall do you want the hollow square"
# width = int(raw_input())

# for i in range(height):
#     if i == 0:
#         print '*' * width
#     elif i == height -1:
#         print '*' * width
#     else:
#         empy_space = ' '
#         between = '*' + empy_space * (width -2) + '*'
#         print between


# def triangle(num,t=-1):
# 	for i in range(0,num):
# 		print ' ' * (num-1) + '*'*(t+2)
# 		t=t+2
# 		num = num-1
# print "provide a triangle height"
# num = int(raw_input())
# triangle(num)


# for i in range(1,11):
# 	for j in range(1,11):
# 		print str(i) + "x" + str(j) + "=" + str(i*j)


# hollow square with user input

# height = 3
# print "enter text"
# text = raw_input()
# width = len(text)

# for i in range(height):
#     if i == 0:
#         print ('*' * width) + ('*' * 2) 
#     elif i == height -1:
#         print ('*' * width) + ('*' * 2) 
#     else:
#         empy_space = ' '
#         between = '*' + text + '*'
#         print between

# leet_string = "leet"
# leet_string_as_list = list(leet_string)
# leet_speak = ""
# for character in leet_string_as_list:
#    if (character.upper() == "A"):
#       leet_speak += "4"
#    elif (character.upper() == "E"):
#       leet_speak += "3"
#    elif (character.upper() == "G"):
#       leet_speak += "6"
#    elif (character.upper() == "I"):
#       leet_speak += "1"
#    elif (character.upper() == "O"):
#       leet_speak += "0"
#    elif (character.upper() == "S"):
#       leet_speak += "5"
#    elif (character.upper() == "T"):
#       leet_speak += "7"
#    else:
#       leet_speak += character

# print leet_speak

# string_to_test = "spoon"
# result = ""
# current = ""
# previous = ""

# for i in range(0,len(string_to_test)):
#    current = string_to_test[i]
#    if (current == previous):
#       result = result + 4 * current
#    else:
#       result = result + current
#    previous = current
# print result




# def decrypt_function(encrypted_letter):
#    try:
#       number = encrypted_list.index(encrypted_letter)
#    except ValueError:
#       decrypted_message.append(encrypted_letter)
#    else:
#       decrypted_message.append(decrypted_list[number])

# message = "lbh zhfg hayrnea jung lbh unir yrnearq"
# decrypted = "abcdefghijklmnopqrstuvwxyz "
# encrypted = "nopqrstuvwxyzabcdefghijklm "
# message_list = list(message)
# decrypted_list = list(decrypted)
# encrypted_list = list(encrypted)
# decrypted_message = []

# for i in range(0,len(message_list)):
#    decrypt_function(message_list[i])
# decrypted_message_string = "".join(decrypted_message)
# print decrypted_message_string




# dictionary = {
#    'a': 1,
#    'b': 1
# }

# alphabet = ['a','b','c']

# for letter in alphabet:
#    if letter in dictionary:
#       print (letter + ' is in dictionary')
#    else:
#       print (letter + ' is NOT in dictionary')


original_dict = {
   'a': 1,
   'b': 2,
   'c': 3,
   'd': 4
}
new_dict = {}

top_three = {}

# print top_three['a']

# while len(top_three) < 4:
#     for key in original_dict:
#         top_three[max(original_dict)] = original_dict[max(original_dict)]
#         del original_dict[key]
        
# print top_three

####################################

########### GLOBAL SCOPE ###########

####################################

x = 3
y = 0 ## globally set y = 0
def get_number():
  global y
  y = 5 ## globally change y to 5, because you put 'global y'

get_number()
print y ## y was set to 5 globally in the function, so y will be 5


user_input = raw_input("enter a number")
try:
  convert_user = int(user_input)
except ValueError:
  print "You must enter a number"
else:
  print "You entered %d" % convert_user
