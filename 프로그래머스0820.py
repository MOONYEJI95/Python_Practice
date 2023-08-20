arr = [0,1,2,4,3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

# 방법1
def solution(arr, queries):
    answer = []
    answer_final = []
    queries_i=[]
    for i in range(len(queries)) :
        queries_i.append(list(range(queries[i][0],queries[i][1]+1)))      

    for i in range(len(queries_i)) :
        for j in queries_i[i] :
            if queries[i][2] < arr[j] :
                answer.append(arr[j])
        if answer==[] : 
            answer_final.append(-1)
        else :
            answer_final.append(min(answer))
        answer=[]
    return print(answer_final)
solution(arr, queries)

# 방법2

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return print(answer)