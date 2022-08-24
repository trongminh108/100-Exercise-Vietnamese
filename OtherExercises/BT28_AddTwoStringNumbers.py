"""
Định nghĩa hàm có thể nhận hai số nguyên trong dạng chuỗi
và tính tổng của chúng, sau đó in tổng ra giao diện 
điều khiển.
"""

def AddTwoStringNumbers(a=0, b=0):
    return int(a) + int(b)

if __name__ == "__main__":
    while True:
        try:
            a, b = map(str, input("Enter the number: ").split())
            break
        except:
            print("\nTry Again")

    print("Result:", AddTwoStringNumbers(a, b))

    
    
    
    
    

    
        
    