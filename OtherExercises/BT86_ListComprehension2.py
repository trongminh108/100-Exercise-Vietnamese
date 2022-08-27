"""
Sử dụng list comprehension để viết chương trình in list 
sau khi đã loại bỏ các số chia hết cho 5 và 7 trong 
[12,24,35,70,88,120,155].

Gợi ý: Giống bài 85.
"""

#use function programming
def BT86_Show(list_nums):
    check = lambda x: x%5!=0 and x%7!=0
    return list(filter(check, list_nums))

#use list comprehension
def BT86_ListComprehension(list_nums):
    return [num for num in list_nums if num%5!=0 and num%7!=0]

if __name__ == "__main__":
    list_nums = [12, 24, 35, 70, 88, 120, 155]
    print(BT86_Show(list_nums))
    print(BT86_ListComprehension(list_nums))
    
    
    
   

    