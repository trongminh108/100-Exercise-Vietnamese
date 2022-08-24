"""
Định nghĩa một hàm có thể chuyển số nguyên thành chuỗi 
và in nó ra giao diện điều khiển
"""





def ConvertIntToString(num):
    return str(num)

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the number: "))
            break
        except:
            print("\nTry Again")

    print("Convert completed:" + ConvertIntToString(num))

    
    
    
    
    

    
        
    