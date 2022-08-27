"""
Viết chương trình xuất ra một số chẵn ngẫu nhiên trong 
khoảng 0 đến 10 (bao gồm cả 0 và 10), 
sử dụng module random và list comprehension.

Gợi ý:
Sử dụng random.choice() để tạo một phần tử ngẫu nhiên 
từ list
"""

from random import choice

def BT76_Show(num=200):
    list_nums = [i for i in range(0, num+1, 7) if i%5==0]
    return choice(list_nums)

if __name__ == "__main__":

    # for i in range(10000000):
    #     x = BT74_CreateRandomNum()
    #     if x > 95 or x < 5:
    #         print(x)
    print(BT76_Show())
    
   

    