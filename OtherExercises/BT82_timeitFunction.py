"""
Bạn hãy viết một chương trình để in thời gian thực thi 
(running time of execution) phép tính "1+1" 100 lần.

Gợi ý: Sử dụng timeit() để đo thời gian chạy
"""

from timeit import Timer

def BT82_Show():
    return Timer("for i in range(100): 1+1").timeit()

if __name__ == "__main__":
    print(BT82_Show())
    
    
   

    