"""
Viết chương trình sắp xếp tuple (name, age, score) 
theo thứ tự tăng dần, name là string, age và height 
là number. Tuple được nhập vào bởi người dùng. 
Tiêu chí sắp xếp là:

Sắp xếp theo name sau đó sắp xếp theo age,
sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.

Nếu đầu vào là:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Thì đầu ra sẽ là:
[('John', '20', '90'), 
('Jony', '17', '91'), 
('Jony', '17', '93'), 
('Json', '21', '85'), 
('Tom', '19', '80')]
"""

from operator import itemgetter

def BT22_Show(list_name):
    list_name.sort(key=itemgetter(0, 1, 2))
    return list_name

if __name__ == "__main__":
    list_name = []
    while True:
        infor = input("Enter your information: ")
        
        if infor.lower() == "quit":
            break

        check = [", ", ",", " "]
        for c in check:
            if c in infor:
                infor = tuple(infor.split(c))
                break
        list_name.append(infor)
        
    print(BT22_Show(list_name))
        
    
    
    
    
    
    

    
        
    