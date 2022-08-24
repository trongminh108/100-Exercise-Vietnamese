"""
Viết comment đặc biệt để chỉ định file code nguồn 
Python ở Unicode
"""

def BT64_Show(num):
    res = 0
    for i in range(1, num+1):
        res += i/(i+1)
    return res


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the positive number: "))
            if num <= 0:
                raise ValueError
            break
        except:
            print("\nTry Again!")

    print(f"The inverse of number from 1 to {num}: {BT64_Show(num)}")