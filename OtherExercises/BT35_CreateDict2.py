"""
Định nghĩa một hàm có thể tạo ra một dictionary chứa key 
là những số từ 1 đến 20 (bao gồm cả 1 và 20) 
và các giá trị bình phương của key. 
Hàm chỉ cần in các key.
"""

def BT35_Show(num):
    res = dict()
    for i in range(1, num+1):
        res[i] = i**2
    return res.keys()

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT35_Show(num))

    
    
    
    
    

    
        
    