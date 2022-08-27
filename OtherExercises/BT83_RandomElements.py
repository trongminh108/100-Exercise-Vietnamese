"""
Viết chương trình để trộn và in list [3,6,7,8].

Gợi ý: Sử dụng shuffle() để trộn list.
"""

from random import shuffle

def BT83_Show(list_nums):
    shuffle(list_nums)
    return list_nums

if __name__ == "__main__":
    lst = [i for i in range(11)]
    print(BT83_Show(lst))
    
    
   

    