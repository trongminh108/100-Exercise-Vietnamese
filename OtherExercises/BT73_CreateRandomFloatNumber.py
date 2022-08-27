"""
Tạo một số thập phân ngẫu nhiên, có giá trị nằm trong khoảng 
từ 10 đến 100 bằng cách sử dụng module math của Python.

Gợi ý: Sử dụng random.random() 
để tạo float ngẫu nhiên trong [0,1]
"""



from random import random

def BT73_CreateRandomNum():
    return (random() + 0.1) * 90.9

if __name__ == "__main__":
    print(BT73_CreateRandomNum())

    
   

    