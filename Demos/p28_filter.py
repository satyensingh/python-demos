
list = [1, 2, 3, 4, 5]

even_list = filter(lambda x : x%2==0, list)
print(even_list)

odd_list = filter(lambda x : x%2!=0, list)
print(odd_list)
