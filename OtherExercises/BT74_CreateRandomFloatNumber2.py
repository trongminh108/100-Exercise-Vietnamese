"""
Tạo một số thập phân ngẫu nhiên, có giá trị nằm trong 
khoảng 5 đến 95, sử dụng module math của Python.

Gợi ý: Giống bài 73.
"""



from random import random

def BT74_CreateRandomNum():
    res = random()
    if res < 0.05:
        res += 0.05
    elif res > 0.95:
        res -= 0.9
    return res * 100

if __name__ == "__main__":

    # for i in range(10000000):
    #     x = BT74_CreateRandomNum()
    #     if x > 95 or x < 5:
    #         print(x)
    print(BT74_CreateRandomNum())
    
   

    