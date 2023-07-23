text = input("문자열을 입력하세요 : ")

# 공백제거
text1 = text.replace(" ","")
print(text1)

# 대문자로 변경
text2 = text1.upper()
print(text2)

# 특수문자 제거
import re
text3 = re.sub("[^A-Z가-힣0-9]","",text2)
print(text3)

# 거꾸로 출력
text4 = text3[::-1]
print(text3)

# 일치 여부
if text3==text4 :
    print(True)
else :
    print(False)