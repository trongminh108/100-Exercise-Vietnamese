"""
Viết chương trình để in một số nguyên ngẫu nhiên từ 
7 đến 15.

Gợi ý: Sử dụng random.randrange() để lấy số nguyên 
ngẫu nhiên trong một phạm vi nhất định.
"""

from random import randrange

def BT80_Show(left=7, right=15):
    return randrange(left, right+1)

if __name__ == "__main__":
    
    print(BT80_Show())
    
   

    