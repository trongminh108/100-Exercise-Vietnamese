"""
Viết một chương trình tìm tất cả các số trong đoạn 
1000 và 3000 (tính cả 2 số này) sao cho tất cả 
các chữ số trong số đó là số chẵn. In các số tìm được 
thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập 
vào chương trình nó nên được giả định là dữ liệu 
được người dùng nhập vào từ giao diện điều khiển.
"""

def Check(s):
    for num in s:
        if int(num) % 2 != 0:
            return False
    return True

def BT15_Show(a=1000, b=3000):
    for i in range(a, b, 2):
        if Check(str(i)):
            print(i, end=", ")

if __name__ == "__main__":
    BT15_Show()
   
    
    
    

    
        
    