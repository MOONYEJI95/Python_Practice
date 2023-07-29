#1
str1="aaaaa"
str2="bbbbb"

a = ""
for i in range(len(str1)) :
    a = a + str1[i] + str2[i]
print(a)

#2
arr = ["a","b","c"]
txt = ""
for i in range(len(arr)) :
    txt = txt + arr[i]
print(txt) 
#2 다른방법
print(''.join(arr))

#3
my_string = "string"
k = 3

answer = ''
answer = my_string * k
print(answer)

#4

ineq = ">"
eq = "!"
n = 41
m = 78

if ineq+eq == "<=" :
    if n<=m :
        print(1)
    else :
        print(0)
if ineq+eq == ">=" :
    if n>=m :
        print(1)
    else :
        print(0)
if ineq+eq == "<!" :
    if n<m :
        print(1)
    else :
        print(0)
if ineq+eq == ">!" :
    if n>m :
        print(1)
    else :
        print(0)      

#4 다른방법
print(int(eval(str(n)+ineq+eq.replace('!','')+str(m))))

if ineq+eq == "<=" :
    print(int(n<=m))
if ineq+eq == ">=" :
    print(int(n>=m))
if ineq+eq == "<!" :
    print(int(n<m))
if ineq+eq == ">!" :
    print(int(n>m))
