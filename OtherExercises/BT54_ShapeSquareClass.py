"""
Định nghĩa một class có tên là Shape và class con là 
Square. Square có hàm init để lấy đối số là chiều dài. 
Cả 2 class đều có hàm area để in diện tích của hình, 
diện tích mặc định của Shape là 0.

Gợi ý:
Để ghi đè một method trong super class, 
chúng ta có thể định nghĩa một method có
cùng tên trong super class.
"""

class Shape:
    def __init__(self) -> None:
        pass

    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__()
        self.length = length
    
    def Area(self):
        return self.length**2


if __name__ == "__main__":
    sq = Square(5)
    print(sq.Area())

    
    
    
    
    

    
        
    