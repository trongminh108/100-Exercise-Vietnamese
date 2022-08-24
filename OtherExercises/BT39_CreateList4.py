"""
Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 
đến 20 (bao gồm cả 1 và 20). 
Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.
"""

def BT39_Show(num):
    res = [i**2 for i in range(1, num+1)]
    return res[5:]

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT39_Show(num))

    
    
    
    
    

    
        
    