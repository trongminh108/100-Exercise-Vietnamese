"""
Viết chương trình in list sau khi đã xóa giá trị 24 
trong [12,24,35,24,88,120,155].

Gợi ý: Sử dụng phương thức xóa của list để xóa giá trị.
"""


def BT90_Show(list_nums, key=24):
    list_nums.remove(key)
    return list_nums

if __name__ == "__main__":
    list_nums = [12, 24, 35, 70, 88, 120, 155]
    print(BT90_Show(list_nums, 24))
    
    
    
   

    