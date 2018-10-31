import re

input = "Ramesh,21,1800-100-200"

w = input.split(",")
print(w)
print(w[2])

# . -> any character/number/symbols
# [01] -> 0 or 1
# [0-9] -> everything from 0 to 9 and one occurrences
# * -> 0 or more occurences
# + -> 1 or more occurences
# ? -> 0 or 1 occurences
# () -> grouping the matched values to access using group()/group(index) function
# ^ -> not, should appear at first place in brackets/set
# 

matches = re.match(r'(.*)-100-(.*)', w[2])

#Refer photos