"""
Viết chương trình in list sau khi xóa các số chẵn trong 
[5,6,77,45,22,12,24].

Gợi ý: Sử dụng list comprehension để xóa một loạt phần tử 
của list.
"""

def BT85_Show(list_nums):
    check = lambda x: x%2!=0
    return list(filter(check, list_nums))

if __name__ == "__main__":
    list_nums =  [5, 6, 77, 45, 22, 12, 24]
    print(BT85_Show(list_nums))
    
    
   

    