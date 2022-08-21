"""
Viết một chương trình có 2 chữ số, X, Y nhận giá trị 
từ đầu vào và tạo ra một mảng 2 chiều. 
Giá trị phần tử trong hàng thứ i và cột thứ j của 
mảng phải là i*j.
Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: 
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""
def Show(matrix):
    print()
    for row in matrix:
        for val in row:
            print(f"{val:3d}", end="")
        print()

def BT10_Show(x, y):
    res = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(i*j)
        res.append(temp)
    return Show(res)

if __name__ == "__main__":
    while True:
        try:
            x, y = map(int, input("Enter x, y: ").split())
            break
        except:
            print("\nTry Again!")
    
    BT10_Show(x, y)    
    

    
        
    