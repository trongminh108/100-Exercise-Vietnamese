"""
Định nghĩa một lớp gồm có tham số lớp 
và có cùng tham số instance
"""

class Person:
    name = "Person"
    def __init__(self, name = None) -> None:
        self.name = name

if __name__ == "__main__":
    n1 = Person("trong")
    print(n1.name)

    n2 = Person()
    print(n2.name)

    print(Person.name)

    
        
    