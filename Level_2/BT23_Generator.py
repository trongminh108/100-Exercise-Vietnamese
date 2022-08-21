"""
Xác định một class với generator có thể lặp lại các 
số nằm trong khoảng 0 và n, và
chia hết cho 7.
"""

class Generator:
    def __init__(self, n=20) -> None:
        self.max = n
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.count
        self.count += 1
        if x % 7 == 0:
            return x
        if x > self.max:
            raise StopIteration
        return self.__next__()
        



if __name__ == "__main__":
    num = int(input("Enter the number: "))
    obj = Generator(num)
    for i in obj:
        print(i)
        
    
    
    
    
    
    

    
        
    