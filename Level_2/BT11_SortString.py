"""
Viết một chương trình chấp nhận chuỗi từ do người 
dùng nhập vào, phân tách nhau
bởi dấu phẩy và in những từ đó thành chuỗi theo 
thứ tự bảng chữ cái, phân tách
nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: 
without,hello,bag,world, thì đầu ra sẽ là: 
bag,hello,without,world.

"""
def BT11_Show(list_string):
    return ", ".join(sorted(list_string))
    
    

if __name__ == "__main__":
    while True:
        try:
            strings = input("Enter the words: ").split(", ")
            break
        except:
            print("\nTry Again!")
    
    print(BT11_Show(strings)) 
    

    
        
    