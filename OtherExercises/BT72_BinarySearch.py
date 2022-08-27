"""
Viết hàm tìm kiếm nhị phân để tìm các item trong một 
list đã được sắp xếp. Hàm sẽ trả lại chỉ số của phần tử 
được tìm thấy trong list.

Gợi ý: Sử dụng if/elif để giải quyết các điều kiện.
"""



def BT72_BinarySearch(key, list_nums):
    left = 0
    right = len(list_nums)
    while right >= left:
        mid = (left+right) // 2
        if mid >= len(list_nums):
            return -1
        if list_nums[mid] == key:
            return mid
        elif list_nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    list_nums = [i for i in range(1, 11)]
    while True:
        try:
            key = int(input("Enter your key: "))
            break
        except:
            print("\nTry Again!")

    idx = BT72_BinarySearch(key, list_nums)
    if idx != -1:
        print(f"Key {key} in index: {idx}")
    else:
        print(f"Key {key} not in list")


    
   

    