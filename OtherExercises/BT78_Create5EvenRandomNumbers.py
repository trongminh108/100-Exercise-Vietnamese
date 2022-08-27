"""
Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn 
nằm trong đoạn [100;200].

Gợi ý: Giống bài 77.
"""

from random import sample

def BT78_Show(left=100, right=200):
    return sample(range(left, right+1, 2), 5)

if __name__ == "__main__":
    print(BT78_Show())
    
   

    