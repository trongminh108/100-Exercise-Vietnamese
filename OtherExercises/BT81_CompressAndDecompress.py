"""
Viết chương trình để nén và giải nén string
"hello world!hello world!hello world!hello world!".

Gợi ý: Sử dụng zlib.compress() và zlib.decompress() 
để nén và giải nén string.
"""

import zlib

def BT81_Show(string):
    t = zlib.compress(string.encode("utf-8"))
    print(t)
    print(zlib.decompress(t))

if __name__ == "__main__":
    string = "hello world!hello world!hello world!hello world!"
    
    BT81_Show(string)
    
   

    