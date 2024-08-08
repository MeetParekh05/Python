'''
l1 = [1 , 2 , 3 , [4 , 5 , 6] , "Python"]
print(l1[0])
print(l1[3][1])
print(l1[-1][1:])
print(l1[-1][-1][1:])
'''
'''
l1 = [1 , 2 , 3 , [4 , 5 , "Python"]]
l1.append("Programming")
l1[-1].append("Programming")
print(l1)
'''
'''
l1 = [1 , 2 , 3 , [30 , 20 , 50]]
l1[-1].sort()
print(l1)
'''
'''
l2 = ["x" , "y" , "a" , "f" , "h" ]
l2.sort()
l2.reverse()
l2.insert(2,"w")
print(l2) 
'''
'''
l1 = [10,20,30,[50,60,[70,80]]]
print(l1[-1][-1][1])
'''
'''
l1 = [10,20,30,[50,60,["python","program"]]]
print(l1[3][2][0] , l1[3][-1][-1])
'''

import math

l1 = [10,20,30,[50,60,[100,200]]]
inner_list = l1[3][2]
sqrt_100 = math.sqrt(inner_list[0])
sqrt_200 = math.sqrt(inner_list[1])
l1.insert (inner_list , sqrt_100)
l1.insert(inner_list , sqrt_200)
print(sqrt_100)
print(sqrt_200)
print(l1)


