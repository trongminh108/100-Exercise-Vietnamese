"""
Viết chương trình in list sau khi đã xóa số ở vị trí 
thứ 0, thứ 4, thứ 5 trong [12,24,35,70,88,120,155].

Gợi ý: Giống bài 87.
"""



def BT89_Show(list_nums):
    check = {0, 4, 5}
    return [x for i, x in enumerate(list_nums) if i not in check]

if __name__ == "__main__":
    list_nums = [12, 24, 35, 70, 88, 120, 155]
    print(BT89_Show(list_nums))
    
    
    
   

    