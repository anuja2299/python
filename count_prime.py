def count_primes(num):
    prime = [2]
    count = 1
    flag = False
    for num in range(2,num+1):
        for i in range(2,num):
            if num%i ==0:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            count = count + 1
            prime.append(num)
        else:
            pass
    print(prime)
    return count
