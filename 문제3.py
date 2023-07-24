paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

# 문제 : 금지 단어를 제외하고 나머지 단어 중 가장 흔한 단어 찾기
# 해결 순서 생각하기
# 1. 특수문자 제거(정규식 이용하면 될듯!)
# 2. 대소문자 섞여 있으니 소문자로 통일하기
# 3. 공백을 기준으로 split 해서 리스트 만들기
# 4. 리스트에서 금지단어를 삭제하기
# 5. 최빈값 찾기

# 특수문자 제거
import re
text = re.sub("[^A-Za-z가-힣0-9 ]","",paragraph) # 공백 넣어야 공백이 사라지지 않음!!!
#print(text)
# 소문자 통일
text1 = text.lower()
#print(text1)
# 공백을 기준으로 list 만들기
text2 = list(text1.split(" "))
#print(text2)
# 금지단어 삭제
text2 = [ i for i in text2 if i not in banned]
#print(text2)
# 최빈값 구하기
from collections import Counter
c = Counter(text2)
#print(help(Counter))
#print(dir(Counter))
print(c.most_common(1)[0][0]) # print(c.most_common(1)[0]) 아님!!! [0][0]으로 들고와야 함





