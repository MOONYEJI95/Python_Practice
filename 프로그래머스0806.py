#1
num_list=[2, 1, 6]

num_list_len=len(num_list)
if num_list[num_list_len-1]-num_list[num_list_len-2] >=0 :
    num_list.append(num_list[num_list_len-1]-num_list[num_list_len-2])
    print(num_list)
else :
    num_list.append(num_list[num_list_len-1] * 2)
    print(num_list)


#2
n=0
control = "wsdawsdassw"
w_count = control.count("w")
a_count = control.count("a")
s_count = control.count("s")
d_count = control.count("d")

print(n+w_count+a_count*(-10)+s_count*(-1)+d_count*10)

#3
numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
answer = ''
for i in range(len(numLog)-1) :
    if numLog[i+1]-numLog[i] == 1 :
        answer = answer+'w'
    elif numLog[i+1]-numLog[i] == -1 :
        answer = answer+'s'
    elif numLog[i+1]-numLog[i] == 10 :
        answer = answer+'d'
    elif numLog[i+1]-numLog[i] == -10 :
        answer = answer+'a'
print(answer)

#4
arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]


for k in range(len(queries)) :
    temp = ''
    temp = arr[queries[k][0]]
    arr[queries[k][0]] = arr[queries[k][1]]
    arr[queries[k][1]] = temp
print(arr)

# 4-다른방법
arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]

for k in range(len(queries)) :
    arr[queries[k][0]],arr[queries[k][1]] = arr[queries[k][1]],arr[queries[k][0]]
print(arr)

# 4-다른방법2
arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]

for i, j in queries :
    arr[i], arr[j] = arr[j], arr[i]
print(arr)