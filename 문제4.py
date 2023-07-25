import pandas as pd

text = ["eat", "tea", "tan", "ate", "nat", "bat"]
text1=[]
text_final=[]

for i in range(len(text)) :
    a = ''.join(sorted(text[i]))
    text1.append(a)

text3 = pd.Series(text1)
text5 = pd.Series(text)
text2 = set(text1)

for j in text2 :
    text_final.append(text5[text3 == j].tolist())
print(text_final)



"""
# 답안

import collections

def solution(text) :

    anagrams = collections.defaultdict(list)
    for word in text :
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(solution(text))        


"""


