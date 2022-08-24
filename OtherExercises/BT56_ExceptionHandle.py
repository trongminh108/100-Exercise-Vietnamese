"""
Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.

Gợi ý: Sử dụng try/exception để bắt lỗi.
"""



def Error():
    return 5/0

if __name__ == "__main__":
    try:
        Error()
    except Exception as problem:
        print(problem)
    finally:
        print("The calculation canceled")
    
    
    
    

    
        
    