list_one = ["Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"]
list_two = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
result1 = sum(list_two[0])/len(list_two[0])
result2 = sum(list_two[1])/len(list_two[1])
result3 = sum(list_two[2])/len(list_two[2])
result4 = sum(list_two[3])/len(list_two[3])
result5 = sum(list_two[4])/len(list_two[4])
dict = {list_one[0]: result1, list_one[1]: result2, list_one[2]: result3, list_one[3]: result4, list_one[4]: result5}
print(dict)

