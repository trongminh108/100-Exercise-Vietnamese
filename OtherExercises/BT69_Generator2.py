"""
Viết chương trình sử dụng generator để in số chia hết 
cho 5 và 7 giữa 0 và n, cách nhau bằng dấu phẩy, 
n được người dùng nhập vào.

Ví dụ: Nếu n=100 được nhập vào thì đầu ra của 
chương trình là: 0,35,70.

Gợi ý:
Như bài 68.
"""

#use yield
def Generator(num):
    for i in range(0, num+1, 7):
        if i%5==0:
            yield i

def BT69_Show(num):
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
        x = self.count
        self.count += 7
        if x%5==0:
            return x
        return self.__next__()

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

    print(f"Numbers divisible by 5 and 7 from 0 to {num}:", BT69_Show(num))
    gen = ClassGenerator(num)
    print(f"Numbers divisible by 5 and 7 from 0 to {num} (use class):", gen)

    