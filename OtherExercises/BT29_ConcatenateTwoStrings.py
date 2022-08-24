"""
Định nghĩa hàm có thể nhận 2 chuỗi từ input và 
nối chúng sau đó in ra giao diện điều khiển
"""

def BT29_Show(s1, s2):
    return s1 + s2

if __name__ == "__main__":
    while True:
        try:
            s1, s2 = map(str, input("Enter the number: ").split())
            break
        except:
            print("\nTry Again")

    print("Result:", BT29_Show(s1, s2))

    
    
    
    
    

    
        
    