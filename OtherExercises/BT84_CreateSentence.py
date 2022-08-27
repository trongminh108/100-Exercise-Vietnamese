"""
Viết một chương trình để tạo tất cả các câu có chủ ngữ 
nằm trong ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"] 
và tân ngữ là ["Bóng đá","Xếp hình"].

Gợi ý: Sử dụng list[index] để lấy phần tử từ list.
"""

def BT84_Show(subject, verb, noun):
    res = []
    for s in subject:
        for v in verb:
            for n in noun:
                res.append(s+" "+v+" "+n+"\n")
    return "".join(res)

if __name__ == "__main__":
    subject = ["Anh","Em"]
    verb = ["Chơi","Yêu"]
    noun = ["Bóng đá","Xếp hình"]
    print(BT84_Show(subject, verb, noun))
    
    
   

    