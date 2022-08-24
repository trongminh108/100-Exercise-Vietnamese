"""
Viết một chương trình Python nhận chuỗi nhập 
vào bởi người dùng, in "Yes" nếu chuỗi là 
"yes" hoặc "YES" hoặc "Yes", nếu không in "No".
"""

def BT44_Show(string):
    check = ["Yes", "YES", "yes"]
    return "Yes" if string in check else "No"

if __name__ == "__main__":
    while True:
        try:
            string = (input("Enter the positive number: "))
            break
        except:
            print("\nTry Again")

    print(BT44_Show(string))

    
    
    
    
    

    
        
    