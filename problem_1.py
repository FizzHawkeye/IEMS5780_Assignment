def problem_1(a, b):
    count = 0
    for i in range(a,b+1):
        if(i%3!=0 and i%5==0):
            count = count + 1
    return count