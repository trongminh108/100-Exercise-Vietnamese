"""
Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm 
đầu tiên (0,0). Robot có thể di chuyển theo hướng 
UP, DOWN, LEFT và RIGHT với những bước nhất định. 
Dấu di chuyển của robot được đánh hiển thị như sau:

UP 5
DOWN 3
LEFT 3
RIGHT 3

Các con số sau phía sau hướng di chuyển chính là 
số bước đi. Hãy viết chương trình để tính toán 
khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, 
sau khi robot đã di chuyển một quãng đường. 
Nếu khoảng cách là một số thập phân chỉ cần in só
nguyên gần nhất.

Ví dụ: Nếu tuple sau đây là input của chương trình:
UP 5
DOWN 3
LEFT 3
RIGHT 2
thì đầu ra sẽ là 2
"""

from math import sqrt


class Robot:
    def __init__(self, pos=[0, 0]) -> None:
        self.pos = pos
    
    def move(self, direction, steps):
        direction = direction.upper()
        if direction == "UP":
            self.pos[1] += steps
        elif direction == "DOWN":
            self.pos[1] -= steps
        elif direction == "RIGHT":
            self.pos[0] += steps
        elif direction == "LEFT":
            self.pos[0] -= steps

    def calculate(self):
        x, y = self.pos
        return round(sqrt(x*x + y*y))

if __name__ == "__main__":
    list_move = [
        ("UP", 5),
        ("DOWN", 3),
        ("LEFT", 3),
        ("RIGHT", 2),
        ("UP", 2)
    ]
    robot = Robot()
    for move in list_move:
        robot.move(*move)
    
    print(robot.calculate())

    
    
    
    
    

    
        
    