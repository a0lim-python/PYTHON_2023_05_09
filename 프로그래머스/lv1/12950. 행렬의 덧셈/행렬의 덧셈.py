def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for num1, num2 in list(zip(arr1[i], arr2[i])):
            answer[i].append(num1 + num2)
    return answer