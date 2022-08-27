"""
Với 2 list cho trước: [12,3,6,78,35,55,120] và 
[12,24,35,24,88,120,155], viết chương trình
để tạo list có phần tử là giao của 2 list đã cho.

Gợi ý: Sử dụng set() và "&=" để thiết lập điểm giao.
"""


def BT91_Show(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    l1 = [12, 3, 6, 78, 35, 55, 120]
    l2 = [12, 24, 35, 24, 88, 120, 155]
    print(BT91_Show(l1, l2))
    
    
    
   

    