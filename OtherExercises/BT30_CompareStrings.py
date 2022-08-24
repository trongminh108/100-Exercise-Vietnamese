"""
Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có 
độ dài lớn hơn trong giao diện điều khiển. 

Nếu 2 chuỗi có chiều dài như nhau 
thì in tất cả các chuỗi theo dòng
"""

def BT30_Show(s1, s2):
    if len(s1) > len(s2):
        return s1
    if len(s1) < len(s2):
        return s2
    return s1 + "\n" + s2

if __name__ == "__main__":
    while True:
        try:
            s1, s2 = map(str, input("Enter the number: ").split())
            break
        except:
            print("\nTry Again")

    print("Result:", BT30_Show(s1, s2))

    
    
    
    
    

    
        
    