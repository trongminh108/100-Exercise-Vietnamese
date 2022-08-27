"""
Viết chương trình để giải 1 câu đố cổ của Trung Quốc: 
Một trang trại thỏ và gà có 35 đầu, 94 chân, 
hỏi số thỏ và gà là bao nhiêu?

Gợi ý: Sử dụng vòng lặp for để lặp qua tất cả các giả thuyết có thể.
"""

def BT96_Show(heads, legs):
    for x in range(heads):
        y = heads - x
        if 2*x + 4*y == legs:
            return (x, y)
    return "None"

if __name__ == "__main__":
    heads, legs = list(map(int, input("Enter heads and legs: ").split()))
    print(BT96_Show(heads, legs))
    
    
   

    