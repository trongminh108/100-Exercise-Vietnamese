"""
Viết chương trình tính tần suất các từ từ input. 
Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.

Giả sử input là: New to Python or choosing between 
Python 2 and Python 3? Read Python 2 or Python 3.

Thì output phải là:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

def BT25_Show(string):
    list_words = sorted(string.split())
    list_words.append(".")
    res = dict()

    count = 1
    for i in range(len(list_words)-1):
        if list_words[i] == list_words[i+1]:
            count += 1
        else:
            res[list_words[i]] = count
            count = 1
    return res

def SampleCode(string):
    dict_fre = {}
    list_words = string.split()
    for word in list_words:
        dict_fre[word] = dict_fre.get(word, 0) + 1
    words = sorted(dict_fre.keys())

    for word in words:
        print(f"{word}: {dict_fre[word]}")
    return

if __name__ == "__main__":
    string = "New to Python or choosing between Python 2 and Python 3? Read\
        Python 2 or Python 3"
    
    print(SampleCode(string))

    
    
    
    
    

    
        
    