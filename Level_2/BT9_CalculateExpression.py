"""
Viết chương trình và in giá trị theo công thức cho trước: 
Q = √([(2 * C * D)/H]) (bằng
chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. 
Với giá trị cố định của C là
50, H là 30. 
D là dãy giá trị tùy biến, 
được nhập vào từ giao diện người dùng, các giá
trị của D được phân cách bằng dấu phẩy.
Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 
100,150,180 thì đầu ra sẽ là 18,22,24
"""

from math import sqrt

def BT9_Show(list_num, c=50, h=30):
    res = []
    for d in list_num:
        temp = round(sqrt((2*c*d)/h))
        res.append(temp)
    return res

if __name__ == "__main__":
    nums = input("Enter the numbers: ").split(', ')
    list_num = []
    for val in nums:
        list_num.append(int(val))
    print(BT9_Show(list_num))
    

    
        
    