"""
Viết các lệnh assert để xác minh rằng tất cả các số 
trong list [2,4,6,8] là chẵn.

Gợi ý: Sử dụng assert để khẳng định.
"""

def BT70_Show(list_nums):
    for num in list_nums:
        assert num % 2 == 0, "There is at least one odd number in list"

if __name__ == "__main__":
    while True:
        try:
            nums = input("Enter any numbers: ").split()
            
            if any (not num.isnumeric() for num in nums):
                raise ValueError

            list_nums = [int(i) for i in nums]
            break
        except:
            print("\nTry Again!")

    try:
        BT70_Show(list_nums)
        print("All numbers in list are even")
    except Exception as problem:
        print(problem)


    
   

    