# How to make deep copy of dictionary

import copy
list1 = [[1,1,1],[2,2,2],[3,3,3]]
new_list = copy.deepcopy(list1)

list1[1][0]='BB'

print("list1:", list1)
print("new list", new_list)


