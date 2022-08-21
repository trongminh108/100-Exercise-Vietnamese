"""
Viết một chương trình chấp nhận đầu vào là một chuỗi 
các từ tách biệt bởi khoảng trắng, 
loại bỏ các từ trùng lặp, 
sắp xếp theo thứ tự bảng chữ cái, 
rồi in chúng.

Giả sử đầu vào là: hello world and practice makes 
perfect and hello world again

Thì đầu ra là: again and hello makes 
perfect practice world

Gợi ý:
- Trong trường hợp dữ liệu đầu vào được nhập 
vào chương trình nó nên được giả định là dữ liệu 
được người dùng nhập vào từ giao diện điều khiển.

- Sử dụng set để loại bỏ dữ liệu trùng lặp tự động 
và dùng sorted() để sắp xếp dữ liệu.

"""
def BT12_Show(list_words):
    res = list(set(list_words))
    res.sort()
    return " ".join(res)
    
    

if __name__ == "__main__":
    while True:
        try:
            strings = input("Enter the string: ").split(" ")
            break
        except:
            print("\nTry Again!")
    
    print(BT12_Show(strings)) 
    

    
        
    