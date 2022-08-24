"""
Định nghĩa 1 hàm có thể tính tổng hai số
"""



def AddTwoNumbers(a=0, b=0):
    return a + b

if __name__ == "__main__":
    while True:
        try:
            a, b = map(int, input("Enter two number: ").split())
            break
        except:
            print("\nTry Again")

    print("Result of two numbers is:", AddTwoNumbers(a, b))

    
    
    
    
    

    
        
    