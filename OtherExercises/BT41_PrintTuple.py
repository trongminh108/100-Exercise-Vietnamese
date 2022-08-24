"""
Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một 
chương trình in một nửa số giá trị đầu tiên trong 1 dòng 
và 1 nửa số giá trị cuối trong 1 dòng.

Gợi ý:
Sử dụng [n1:n2] để lấy một phần từ tuple.
"""

def BT41_Show(tuple_nums):
    print(tuple_nums[:len(tuple_nums)//2])
    print(tuple_nums[len(tuple_nums)//2:])

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            tuple_nums = tuple([i for i in range(1, num+1)])
            break
        except:
            print("\nTry Again")

    BT41_Show(tuple_nums)

    
    
    
    
    

    
        
    