"""
Viết chương trình in list sau khi đã xóa số thứ 0, 
thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155].

Gợi ý:
+ Sử dụng list comprehension để xóa một loạt phần tử 
trong list.
+ Sử dụng hàm enumerate() để lấy index, value của tuple.
"""

def BT87_Show(list_nums):
    check = [0, 2, 4, 6]
    return [x for i, x in enumerate(list_nums) if i not in check]



if __name__ == "__main__":
    list_nums = [12, 24, 35, 70, 88, 120, 155]
    print(BT87_Show(list_nums))
    
    
    
   

    