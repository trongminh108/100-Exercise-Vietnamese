"""
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập 
vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm kiểm tra đơn giản để kiểm tra 
method của class.
Ví dụ: Chuỗi nhập vào là quantrimang.com 
thì đầu ra phải là: QUANTRIMANG.COM
"""

class BT5:
    def getString(self):
        self.s = input("Enter your string: ")
    def printString(self):
        print("Your string: " + self.s.upper())

if __name__ == "__main__":
    bt5 = BT5()
    bt5.getString()
    bt5.printString()