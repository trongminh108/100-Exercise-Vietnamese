"""
Viết một chương trình tính giá trị của a+aa+aaa+aaaa 
với a là số được nhập vào bởi người dùng.

Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
"""

def BT18_Show(num):
    res = eval("a+aa+aaa+aaaa".replace("a", num))
    return "Result: " + str(res)

if __name__ == "__main__":
    a = input("Enter number a: ")
    print(BT18_Show(a))

   
    
    
    

    
        
    