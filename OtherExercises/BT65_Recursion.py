"""
Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và 
f(0)=1, với n là số được nhập vào (n>0).

Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 501.

Gợi ý: Chúng ta có thể định nghĩa hàm đệ quy trong Python.
"""

def BT65_Recursion(num):
    if num == 0:
        return 1
    return BT65_Recursion(num-1) + 100

def BT65_NonRecursion(num):
    return 1 + num*100

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            if num <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The result of f({num})=f({num}-1)+100 with f(0)=1: {BT65_Recursion(num)}")
    print(f"The result of f({num})=f({num}-1)+100 with f(0)=1 (Non Recursion): {BT65_NonRecursion(num)}")
