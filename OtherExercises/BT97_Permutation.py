"""
Viết chương trình in tất cả các hoán vị của [1,2,3].

Gợi ý: Sử dụng itertools.permutations() để lấy hết các 
hoán vị của list
"""

from itertools import permutations


def permutation(list_nums):
    if len(list_nums) == 0:
        return []
    
    if len(list_nums) == 1:
        return [list_nums]

    l = []
    for i in range(len(list_nums)):
       m = list_nums[i]
       remlist_nums = list_nums[:i] + list_nums[i+1:]
       temp = permutation(remlist_nums)
       for p in temp:
           l.append([m] + p)
    return l

def BT97_Show(list_nums):
    return list(permutations(list_nums))

if __name__ == "__main__":
    s = [1, 2, 3]

    print(BT97_Show(s))
    
    
   

    