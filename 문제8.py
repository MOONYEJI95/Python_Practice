#1
def solution(a,b,flag) :
    if flag == True :
        return a + b
    else :
        return a - b
print(solution(-4,7,True))

#2
odd=[]
even=[]
num_list = [3, 4, 5, 2, 1]
for i in range(len(num_list)) :
    if num_list[i]%2 == 1 :
        odd.append(str(num_list[i]))
    else :
        even.append(str(num_list[i]))

odd2 = ''.join(odd)
even2 = ''.join(even)
print(odd2)
print(even2)

print(eval(odd2 + '+' + even2))
