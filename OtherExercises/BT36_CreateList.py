"""
Định nghĩa một hàm có thể tạo và in list chứa các 
giá trị bình phương của các số từ 1 đến 20 
(tính cả 1 và 20).
"""

def BT36_Show(num):
    return [i**2 for i in range(1, num+1)]

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT36_Show(num))

    
    
    
    
    

    
        
    