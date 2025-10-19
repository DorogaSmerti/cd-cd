def check_exam(arr1,arr2):
    score = 0
    for i,j in zip(arr1,arr2):
        if i == j:
            score += 4
        elif i != j:
            score -= 1
    return abs(score)