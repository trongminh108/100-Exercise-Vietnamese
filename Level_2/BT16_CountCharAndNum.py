"""
Viết một chương trình chấp nhận đầu vào là một câu, 
đếm số chữ cái và chữ số trong câu đó. 
Giả sử đầu vào sau được cấp cho chương trình: 
hello world! 123

Thì đầu ra sẽ là:

Số chữ cái là: 10
Số chữ số là: 3

"""


def BT16_Show(string):
    c_alpha = 0
    c_num = 0
    for ch in string:
        if ch.isalpha():
            c_alpha += 1
        elif ch.isnumeric():
            c_num += 1
    
    print("Number of letters: {}".format(c_alpha))
    print("Number of letters: {}".format(c_num))

if __name__ == "__main__":
    string = input("Enter the string: ")
    BT16_Show(string)
   
    
    
    

    
        
    