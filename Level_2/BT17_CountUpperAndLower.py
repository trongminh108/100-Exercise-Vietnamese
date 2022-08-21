"""
Viết một chương trình chấp nhận đầu vào là một câu, 
đếm chữ hoa, chữ thường.

Giả sử đầu vào là: Quản Trị Mạng
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8
"""

def BT17_Show(string):
    c_upper = 0
    c_lower = 0
    for ch in string:
        if ch.isupper():
            c_upper += 1
        elif ch.islower():
            c_lower += 1
    
    print("\nNumber of uppercase letters: {}".format(c_upper))
    print("Number of lowercase letters: {}".format(c_lower))

if __name__ == "__main__":
    string = input("Enter the string: ")
    BT17_Show(string)
   
    
    
    

    
        
    