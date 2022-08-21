"""
Viết chương trình tính số tiền thực của một tài khoản 
ngân hàng dựa trên nhật ký giao dịch được nhập vào từ 
giao diện điều khiển.

Định dạng nhật ký được hiển thị như sau:
D 100
W 200
(D là tiền gửi, W là tiền rút ra).

Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100

Thì đầu ra sẽ là:
500
"""

def BT20_Show(operations):
    res = 0
    for oper in operations:
        temp = oper.split()
        if temp[0] == "D":
            res += int(temp[1])
        elif temp[0] == "W" and res >= int(temp[1]):
            res -= int(temp[1])
    return res         


if __name__ == "__main__":
    operations = ["D 300", "D 300", "W 200", "D 100"]
    print(BT20_Show(operations))
    
    
    
    
    

    
        
    