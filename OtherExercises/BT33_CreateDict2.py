"""
Định nghĩa một hàm có thể in dictionary chứa key 
là các số từ 1 đến 3 (bao gồm cả hai số) 
và các giá trị bình phương của chúng.
"""

def BT33_Show(num):
    res = dict()
    for i in range(1, num+1):
        res[i] = i**2
    return res

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT33_Show(num))

    
    
    
    
    

    
        
    