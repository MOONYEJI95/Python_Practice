def solution(code) :
    mode = 0
    ret=''
    for i in range(len(code)) :
        if mode == 0 and code[i] !='1' and i%2==0 :
            ret = ret + code[i]
        elif mode == 0 and code[i] == '1' :
            mode = 1
        elif mode == 1 and code[i] !='1' and i%2==1 :
            ret = ret + code[i]
        elif mode == 1 and code[i] =='1' :
            mode = 0
        else : 
            pass

    if ret == ''  :
        ret = "EMPTY"
    print(ret)    
    
solution("abc1abc1abc")
