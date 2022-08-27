"""
Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, 
chia hết cho 5 và 7, nằm trong đoạn [1;1000].

Gợi ý: Giống bài 77, 78.
"""

from random import sample

def BT79_Show(left=1, right=1000):
    list_nums = [i for i in range(0, right+1, 7) if i%5==0 and i!=0]
    return sample(list_nums, 5)

if __name__ == "__main__":
    print(BT79_Show())
    
   

    