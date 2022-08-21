"""
Sử dụng một danh sách để lọc các số lẻ từ danh sách 
được người dùng nhập vào.

Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 
thì đầu ra phải là: 1,3,5,7,9
"""

def BT19_Show(list_num):
    res = []
    for val in list_num:
        if int(val) % 2:
            res.append(str(val))
    return ", ".join(res) 

if __name__ == "__main__":

    list_num = input("Enter the numbers: ").split(", ")
    print(BT19_Show(list_num))
   
    
    
    

    
        
    