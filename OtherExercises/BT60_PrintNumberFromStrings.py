"""
Viết một chương trình chấp nhận chuỗi từ được phân 
tách bằng khoảng trống và in các từ chỉ gồm chữ số.

Ví dụ: Nếu những từ sau đây là đầu vào của chương trình: 
3 quantrimang.com và 2 python. 
Đầu ra sẽ là ['3', '2']

Gợi ý: Sử dụng re.findall() để tìm tất cả chuỗi con sử dụng 
regex (biểu thức tiêu chuẩn).
"""

# import re
# s = input()
# print(re.findall("\d+", s))


def BT60_Show(list_strings):
    res = []
    for s in list_strings:
        if s.isnumeric():
            res.append(s)
    return res

if __name__ == "__main__":
    while True:
        try:
            s = input("Enter strings separated by spaces: ")
            list_strings = s.split()
            break
        except:
            print("\nTry Again!")

    print(BT60_Show(list_strings))
    
    
    
    

    
        
    