# lambda function to to get the square number for one use only.
print(list(map(lambda num: num ** 2, [1,2,3,4,5,6,7,8,9])))


#lambda function tha can used only for one time to get the num by ascending order by the second number(first, second).



collection_of_num = [(0, 2), (5, 2), (9, 9), (10, -1), (11, -2), (7, 1) , (5, 4)]
collection_of_num.sort(key=lambda x: x[1])

print(collection_of_num)