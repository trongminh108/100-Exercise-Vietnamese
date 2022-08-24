"""
Định nghĩa hàm có thể chấp nhận input là số nguyên 
và in "Đây là một số chẵn" nếu nó chẵn và 
in "Đây là một số lẻ" nếu là số lẻ.
"""

def BT31_Show(num):
    if num % 2 == 0:
        return f"{num} is even number"
    elif num % 2 == 1:
        return f"{num} is odd number"
    return "This is zero"

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT31_Show(num))

    
    
    
    
    

    
        
    