string = "Cheese"
# print string.upper()
# print string.title()
# print string[::-1]


replacements = (('A','4'), ('E','3'), ('G','6'), ('I','1'), ('O','0'), ('S','5'), ('T','7'))
new_string = string.upper()
for old, new in replacements:
	new_string = new_string.replace(old, new)

print new_string


# from string import maketrans
# intab = "AEGIOST"
# outtab = "4361057"
# trantab = maketrans(intab,outtab)
# print string.upper().translate(trantab)

vowel_replace = (('aa','aaaaa'),('ee','eeeee'),('ii','iiiii'),('oo','ooooo'),('uu','uuuuu'))
vow_string = string.lower()
for old, new in vowel_replace:
	vow_string = vow_string.replace(old,new)
print (vow_string)




####################################
####################################
####################################


# String Excercises
string_as_a_string = "This is a string"


# --Leetspeak
characters_to_be_replaced = ["A","E","G","I","O","S","T"]
Characters_to_replace_with = ["4","3","6","1","0","5","7"]
character_replacement_list = []

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

height = 3
print "enter text"
text = raw_input()
width = len(text)

for i in range(height):
    if i == 0:
        print ('*' * width) + ('*' * 2) 
    elif i == height -1:
        print ('*' * width) + ('*' * 2) 
    else:
        empy_space = ' '
        between = '*' + text + '*'
        print between

leet_string = "leet"
leet_string_as_list = list(leet_string)
leet_speak = ""
for character in leet_string_as_list:
   if (character.upper() == "A"):
      leet_speak += "4"
   elif (character.upper() == "E"):
      leet_speak += "3"
   elif (character.upper() == "G"):
      leet_speak += "6"
   elif (character.upper() == "I"):
      leet_speak += "1"
   elif (character.upper() == "O"):
      leet_speak += "0"
   elif (character.upper() == "S"):
      leet_speak += "5"
   elif (character.upper() == "T"):
      leet_speak += "7"
   else:
      leet_speak += character

print leet_speak

string_to_test = "spoon"
result = ""
current = ""
previous = ""

for i in range(0,len(string_to_test)):
   current = string_to_test[i]
   if (current == previous):
      result = result + 4 * current
   else:
      result = result + current
   previous = current
print result

