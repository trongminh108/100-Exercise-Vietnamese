"""
Viết chương trình sử dụng generator để in số chẵn 
trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, 
n là số được nhập vào.

Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình 
là: 0,2,4,6,8,10

Gợi ý: Sử dụng yield để tạo ra giá trị kết tiếp trong 
generator.
"""

#use yield
def Generator(num):
    for i in range(0, num+1, 2):
        yield i

def BT68_Show(num):
    res = []
    for i in Generator(num):
        res.append(str(i))
    return ", ".join(res)

#use class
class ClassGenerator:
    def __init__(self, max) -> None:
        self.max = max
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.max:
            raise StopIteration
        res = self.count
        self.count += 2
        return res

    def __str__(self) -> str:
        res = []
        for i in ClassGenerator(self.max):
            res.append(str(i))
        return ", ".join(res)


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            if num <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"Even numbers from 0 to {num}:", BT68_Show(num))
    gen = ClassGenerator(num)
    print(f"Even numbers from 0 to {num} (use class):", gen)

    