"""
Viết một method tính giá trị bình phương của một số
"""

def square(num):
    return num * num

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter your number: "))
            break
        except:
            print("\nTry again!")

    print(f"Square of {num} is: {square(num)}")
        
    