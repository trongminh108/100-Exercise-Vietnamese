"""
Định nghĩa class có tên là Hinhchunhat được xây dựng 
bằng chiều dài và chiều rộng.

Class Hinhchunhat có method để tính diện tích.

Gợi ý: Như bài 52.
"""

class Rectangle:
    def __init__(self, length=0, width=0) -> None:
        self.length = length
        self.width = width

    def Area(self):
        return self.length*self.width
        

if __name__ == "__main__":
    rec = Rectangle(2, 3)
    print(rec.Area())

    
    
    
    
    

    
        
    