"""
Yêu cầu:
Định nghĩa một class tên Vietnam và class con 
của nó là Hanoi.

Gợi ý: Sử dụng Subclass(ParentClass) 
để định nghĩa một class con.
"""


class Vietnam:
    def __init__(self) -> None:
        print("This is Viet Nam")

class Hanoi(Vietnam):
    def __init__(self) -> None:
        super().__init__()
        print("This is Hanoi")


if __name__ == "__main__":  
    vn = Vietnam()
    hn = Hanoi()

    
    
    
    
    

    
        
    