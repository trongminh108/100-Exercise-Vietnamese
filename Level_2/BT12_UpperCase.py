"""
Viết một chương trình chấp nhận chuỗi là các dòng được 
nhập vào, chuyển các dòng này thành chữ in hoa 
và in ra màn hình. Giả sử đầu vào là:

Hello world
Practice makes perfect

Thì đầu ra sẽ là:
HELLO WORLD
PRACTICE MAKES PERFECT

"""
def BT12_Show(s):
    return s.upper()
    
    

if __name__ == "__main__":
    while True:
        try:
            strings = input("Enter the string: ")
            break
        except:
            print("\nTry Again!")
    
    print(BT12_Show(strings)) 
    

    
        
    