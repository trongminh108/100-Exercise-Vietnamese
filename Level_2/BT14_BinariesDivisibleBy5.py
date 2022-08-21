"""
Viết một chương trình chấp nhận đầu vào là chuỗi các số 
nhị phân 4 chữ số, phân tách bởi dấu phẩy, 
kiểm tra xem chúng có chia hết cho 5 không. 
Sau đó in các số chia hết cho 5 thành dãy phân tách 
bởi dấu phẩy. Ví dụ đầu vào là: 0100,0011,1010,1001

Đầu ra sẽ là: 1010

Gợi ý:

Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả
định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

"""
def BT14_Show(list_binaries):
    res = []
    for bin in list_binaries:
        temp = int(bin, 2)
        if temp % 5 == 0:
            res.append(bin)
    
    print("The number divisible by 5: ", end="")
    return ", ".join(res)
    

if __name__ == "__main__":
    while True:
        try:
            list_binaries = input("Enter the binary numbers: ").split(", ")
            break
        except:
            print("\nTry Again!")
    
    print(BT14_Show(list_binaries)) 
    

    
        
    