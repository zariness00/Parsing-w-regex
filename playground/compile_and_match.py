import re

#defining characters
character_1 = "Dorothy"
character_2 = "Henry"

#compile a reg expression
regular_expression = re.compile("\w{7}")

#checking for a match to char_1 
result_1 = regular_expression.match(character_1)

#storing and printing the matched text here
match_1 = result_1.group(0)
print(match_1)

result_2 = re.match("\w{7}", character_2)
print(result_2)
#the result is Ni=one because I try to match a string with the length of 7, char_2 is less than 7 
