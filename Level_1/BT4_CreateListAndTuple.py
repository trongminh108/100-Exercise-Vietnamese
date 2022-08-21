"""
Viết chương trình chấp nhận một chuỗi số, 
phân tách bằng dấu phẩy từ giao diện
điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 
thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

def BT4_Show(s):
    lst = s.split(',')
    tup = tuple(lst)
    return str(lst) + "\n" + str(tup)

if __name__ == "__main__":
    num = input("Enter the numbers: ")
    print(BT4_Show(num))