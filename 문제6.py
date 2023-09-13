def solution(my_string, overwrite_string, s):

    overwrite_string_len = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+overwrite_string_len:]
    return answer

print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))

