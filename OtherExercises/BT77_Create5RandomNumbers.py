"""
Vui lòng viết chương trình để tạo một list với 5 
số ngẫu nhiên từ 100 đến 200.

Gợi ý: Sử dụng random.sample() để tạo list chứa các giá 
trị ngẫu nhiên.
"""

from random import sample

def BT77_Show(left=100, right=200):
    return sample(range(left, right+1), 5)

if __name__ == "__main__":
    print(BT77_Show())
    
   

    