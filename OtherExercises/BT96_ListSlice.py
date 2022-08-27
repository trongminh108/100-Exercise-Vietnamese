"""
Viết chương trình nhận chuỗi do người dùng nhập vào và 
in các ký tự có chỉ số chẵn.

Ví dụ: Nếu chuỗi sau được nhập vào: q1u2a3n4t5r6i7m8a9n4g5.6c7o8m, thì đầu ra
sẽ là: quantrimang.com.

Gợi ý: Sử dụng list[::2] để lặp list cách 2 vị trí.
"""

def BT96_Show(string):
    return string[::2]

if __name__ == "__main__":
    s = input("Enter the string: ")

    print(BT96_Show(s))
    
    
   

    