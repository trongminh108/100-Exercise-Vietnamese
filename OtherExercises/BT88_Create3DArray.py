"""
Viết chương trình tạo mảng 3D 3*5*8 có mỗi phần tử là 0.

Gợi ý: Sử dụng list comprehension để tạo mảng
"""

def BT88_Show(x=3, y=5, z=8):
    res = []
    t2 = [0] * z
    for i in range(x):
        t1 = []
        for j in range(y):
            t1.append(t2)
        res.append(t1)
    return res


if __name__ == "__main__":
    print(BT88_Show())
    
    
    
   

    