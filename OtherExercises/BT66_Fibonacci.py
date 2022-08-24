"""
Dãy Fibonacci được tính dựa trên công thức sau:
f(n)=0 nếu n=0
f(n)=1 nếu n=1
f(n)=f(n-1)+f(n-2) nếu n>1

Hãy viết chương trình tính giá trị của f(n) với 
n là số được người dùng nhập vào. 

Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của 
chương trình sẽ là 13.

Gợi ý: Tương tự như bài 65, ta cũng sử dụng hàm đệ quy 
trong Python.
"""

def BT66_FibonacciRecursion(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    func = BT66_FibonacciRecursion
    return func(num-1) + func(num-2)

def BT66_FibonacciNonRecursion(num):
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

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            if num <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The fibonacci number in {num} place: {BT66_FibonacciRecursion(num)}")
    print(f"The fibonacci number in {num} place (Non Recursion): {BT66_FibonacciNonRecursion(num)}")
