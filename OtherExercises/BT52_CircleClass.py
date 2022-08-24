"""
Định nghĩa một class có tên là Circle có thể được 
xây dựng từ bán kính. Circle có một method có thể 
tính diện tích.

Gợi ý: Sử dụng def methodName(self) để định nghĩa method.
"""

from math import pi

class Circle:
    def __init__(self, radius=0) -> None:
        self.radius = radius

    def Area(self):
        return round(self.radius**2*pi, 4)

if __name__ == "__main__":
    c = Circle(2)
    print(c.Area())

    
    
    
    
    

    
        
    