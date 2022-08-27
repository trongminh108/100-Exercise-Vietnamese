"""
Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu. 
Tất cả các class có method "getGender" có thể in "Nam" 
cho class Nam và "Nữ" cho class Nu.

Gợi ý: Sử dụng Subclass(Parentclass) để định nghĩa 1 
class con.
"""

class Person:
    def __init__(self) -> None:
        self.gender = None

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self) -> None:
        super().__init__()
        self.gender = "Male"

class Female(Person):
    def __init__(self) -> None:
        super().__init__()
        self.gender = "Female"

if __name__ == "__main__":
    m = Male()
    f = Female()

    print(m.getGender())
    print(f.getGender())
    
    
    
   

    