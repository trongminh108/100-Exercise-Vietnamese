"""
Dãy Fibonacci được tính dựa trên công thức sau:
f(n)=0 nếu n=0
f(n)=1 nếu n=1
f(n)=f(n-1)+f(n-2) nếu n>1

Hãy viết chương trình sử dụng list comprehension để 
in dãy Fibonacci dưới dạng tách biệt bằng dấu ",", 
n được người dùng nhập vào.

Ví dụ: Nếu n được nhập vào là 7 thì đầu ra 
của chương trình sẽ là: 0,1,1,2,3,5,8,13

Gợi ý:
+ Chúng ta có thể định nghĩa hàm đệ quy trong Python.
+ Sử dụng list comprehension để tạo ra list từ list 
hiện có.
+ Sử dụng string.join() để nối danh sách các chuỗi.

"""

def Fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return Fibonacci(num-1) + Fibonacci(num-2)

def FibonacciNonRecursion(num):
    if num <= 2:
        if num == 0:
            return 0
        return 1
    f0 = 0
    f1 = 1
    res = 0
    for _ in range(num-1):
        res = f0 + f1
        f0 = f1
        f1 = res
    return res

def BT67_Show(num, func):
    res = []
    for i in range(num+1):
        res.append(str(func(i)))
    return ", ".join(res)

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            if num <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The fibonacci number in {num} place: {BT67_Show(num, Fibonacci)}")
    print(f"The fibonacci number in {num} place (Non Recursion): {BT67_Show(num, FibonacciNonRecursion)}")
