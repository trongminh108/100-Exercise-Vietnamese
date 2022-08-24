"""
Giả sử rằng chúng ta có vài địa chỉ email dạng 
username@companyname.com, hãy viết một chương trình 
để in username của địa chỉ email cụ thể. 
Cả username và companyname chỉ bao gồm chữ cái.

Ví dụ: Nếu cung cấp địa chỉ email QTM@quantrimang.com 
thì đầu ra sẽ là: QTM.
Trong trường hợp dữ liệu đầu vào không có sẵn, 
ta giả định nó được người dùng
nhập vào từ giao diện điều khiển.

Gợi ý:
Sử dụng \w để kiểm tra chữ cái.
"""

# import re
# emailAddress = input()
# pat2 = "(\w+)@((\w+\.)+(com))"
# re2 = re.match(pat2,emailAddress)
# print (re2.group(1))


def BT58_Show(email):
    if "@" not in email:
        return
    idx = email.index("@")
    return email[:idx]

if __name__ == "__main__":
    mail = "minhtrongpro59@gmail.com"
    print(BT58_Show(mail))
    
    
    
    

    
        
    