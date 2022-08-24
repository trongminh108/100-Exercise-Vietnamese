"""
Viết chương trình Python dùng map() và filter() để tạo 
list chứa giá trị bình phương
của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].

Gợi ý:
+ Dùng map() để tạo list.
+ Dùng filter() để lọc thành phần trong list.
+ Dùng lambda để định nghĩa hàm chưa biết
"""



def BT47_Show(list_nums):
    temp = filter(lambda x: not x%2, list_nums)
    return list(map(lambda x: x*x, temp))

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            list_nums = [i for i in range(1, num+1)]
            if num <= 0:
                raise "Error"
            break
        except:
            print("\nTry Again")

    print(BT47_Show(list_nums))

    
    
    
    
    

    
        
    