"""
Viết chương trình đếm và in số ký tự của chuỗi do người 
dùng nhập vào.

Ví dụ:
Nếu chuỗi nhập vào là quantrimang.com thì đầu ra sẽ là:
q,1
u,1
a,2
n,2
t,1
r,1
i,1
m,2
g,1
.,1
c,1
o,1

Gợi ý:
+ Sử dụng dict để lưu trữ các cặp key/value.
+ Sử dụng dict.get() để tra cứu key với giá trị mặc định.
"""

def BT95_Show(string):
    set_string = set(string)
    res = []
    for s in set_string:
        res.append(f"{s}, {string.count(s)}")
    return "\n".join(res)

def BT95_Show2(string):
    res = dict()
    for ch in string:
        res[ch] = res.get(ch, 0) + 1
    return res

if __name__ == "__main__":
    s = "quantrimang.com"

    print(BT95_Show2(s))
    
    
   

    