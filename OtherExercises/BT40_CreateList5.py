"""
Định nghĩa 1 hàm có thể tạo và in một tuple chứa các 
giá trị bình phương của các số từ 1 đến 20 
(tính cả 1 và 20).

Gợi ý:
+ Sử dụng toán tử ** để lấy giá trị bình phương.
+ Sử dụng range() cho vòng lặp.
+ Sử dụng list.append() để thêm giá trị vào list.
+ Sử dụng tuple() để lấy giá tuple từ list.
"""

def BT40_Show(num):
    return tuple([i**2 for i in range(1, num+1)])

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT40_Show(num))

    
    
    
    
    

    
        
    