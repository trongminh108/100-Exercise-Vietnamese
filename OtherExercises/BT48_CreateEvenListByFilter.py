"""
Viết chương trình Python dùng filter() để tạo danh sách 
chứa các số chẵn trong đoạn
[1,20].

Gợi ý: Giống bài 45.

"""



def BT48_Show(list_nums):
    return list(filter(lambda x: not x%2, list_nums))

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

    print(BT48_Show(list_nums))

    
    
    
    
    

    
        
    