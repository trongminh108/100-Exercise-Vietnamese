"""
Viết một chương trình để tạo tuple khác, 
chứa các giá trị là số chẵn trong
tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
"""

def BT42_Show(tuple_nums):
    return tuple([num for num in tuple_nums if num % 2 == 0])

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            tuple_nums = tuple([i for i in range(1, num+1)])
            break
        except:
            print("\nTry Again")

    print(BT42_Show(tuple_nums))

    
    
    
    
    

    
        
    