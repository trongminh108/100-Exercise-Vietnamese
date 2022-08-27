"""
Viết chương trình nhận chuỗi đầu vào từ giao diện 
điều khiển và in nó theo thứ tự ngược lại.
Ví dụ nếu chuỗi nhập vào là:
i love you
Thì kết quả đầu ra là:
uoy evol i

Gợi ý: Sử dụng list[::-1] để lặp list theo thứ tự ngược lại.
"""

def BT95_Show(string):
    return string[::-1]

if __name__ == "__main__":
    s = input("Enter the string: ")

    print(BT95_Show(s))
    
    
   

    