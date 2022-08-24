"""
Định nghĩa một class exception tùy chỉnh, 
nhận một thông báo là thuộc tính.

Gợi ý: Để định nghĩa một class exception tùy chỉnh, 
chúng ta phải định nghĩa một class kế thừa từ Exception.
"""

class BT57_Error(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

if __name__ == "__main__":
    error = BT57_Error("Oops! Something went wrong!")
    print(error)
    
    
    
    

    
        
    