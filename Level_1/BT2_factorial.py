"""
Viết một chương trình có thể tính giai thừa của một 
số cho trước. Kết quả được in
thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
Ví dụ, số cho trước là 8 thì kết
quả đầu ra phải là 40320.
"""

def factorial(num):
    res = 1
    for i in range(2, num+1):
        res *= i
    return res

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print(factorial(num))