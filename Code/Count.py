def count(n):
    count = 0
    while n > 0:
        count +=1
        n = n // 10
    return count

if __name__=="__main__":
    N = 12345
    print(count(N))
