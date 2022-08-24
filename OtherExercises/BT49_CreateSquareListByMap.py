"""
Viết chương trình Python sử dụng map() để tạo list 
chứa giá trị bình phương của các số trong đoạn [1,20].

Gợi ý: Giống bài 46.

"""



def BT49_Show(list_nums):
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

    print(BT49_Show(list_nums))

    
    
    
    
    

    
        
    