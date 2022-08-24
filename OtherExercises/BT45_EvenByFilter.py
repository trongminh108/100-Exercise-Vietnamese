"""
Viết chương trình Python có thể lọc các số chẵn 
trong danh sách sử dụng hàm filter. 
Danh sách là [1,2,3,4,5,6,7,8,9,10].

Gợi ý:
+ Sử dụng filter() để lọc các yếu tố trong một list.
+ Sử dụng lambda để định nghĩa hàm chưa biết.

"""



def BT45_Show(list_nums):
    return list(filter(lambda x: x%2==0, list_nums))

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            list_nums = [i for i in range(1, num+1)]
            break
        except:
            print("\nTry Again")

    print(BT45_Show(list_nums))

    
    
    
    
    

    
        
    