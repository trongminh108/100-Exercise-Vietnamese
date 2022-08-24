"""
Định nghĩa một hàm có thể tạo ra list chứa các giá trị 
bình phương của các số từ 1
đến 20 (bao gồm cả 1 và 20), 
rồi in 5 mục cuối cùng trong list.
"""

def BT38_Show(num):
    res = [i**2 for i in range(1, num+1)]
    return res[-5:]

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT38_Show(num))

    
    
    
    
    

    
        
    