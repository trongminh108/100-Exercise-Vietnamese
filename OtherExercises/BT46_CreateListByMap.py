"""
Viết chương trình Python dùng map() để tạo list chứa 
các giá trị bình phương của các số trong 
[1,2,3,4,5,6,7,8,9,10].

Gợi ý:
+ Sử dụng map() để tạo list.
+ Sử dụng lambda để định nghĩa hàm chưa biết.
"""



def BT46_Show(list_nums):
    return list(map(lambda x: x*x, list_nums))

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

    print(BT46_Show(list_nums))

    
    
    
    
    

    
        
    