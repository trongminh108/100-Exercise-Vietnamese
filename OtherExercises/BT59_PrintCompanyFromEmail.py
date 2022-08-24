"""
Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để 
lấy companyname.

Gợi ý: Giống bài 58.
"""

# import re
# emailAddress = input()
# pat2 = "(\w+)@(\w+)\.(com)"
# r2 = re.match(pat2,emailAddress)
# print (r2.group(2))


def BT59_Show(email):
    if "@" not in email or "." not in email:
        return
    idx = email.index("@")
    dot = email.index(".")
    return email[idx:dot]

if __name__ == "__main__":
    mail = "minhtrongpro59@AGUgmail.com"
    print(BT59_Show(mail))
    
    
    
    

    
        
    