"""
Viết chương trình in list từ list 
[12,24,35,24,88,120,155,88,120,155], sau khi đã xóa
hết các giá trị trùng nhau.

Gợi ý: Sử dụng set() để lưu trữ các giá trị không 
bị trùng lặp.
"""


def BT92_Show(list_nums):
    return sorted(list(set(list_nums)))

if __name__ == "__main__":
    list_nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    print(BT92_Show(list_nums))
    
    
    
   

    