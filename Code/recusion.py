def print_0_n(n):
    if n < 0:
        return
    print(n)
    print_0_n(n-1)

def print_n_0(n):
    if n<0:
        return
    print_n_0(n-1)
    print(n)

def sum_first_n(n):
    if n == 0:
        return 0
    
    return n + sum_first_n(n -1)

def factorial(n):
    if (n <= 0):
        return 1

    return n * factorial(n-1)

def count_digits(number):
    if number <= 0:
        return 0
    
    return 1 + count_digits( number//10)

def reverse(number):
    if number < 10:
        return n
    digit = number      
    



if __name__=="__main__":
    # print("Hello")
    n = int(input("Enter the number "))
    # print(f"print_0_{n}")
    # print_0_n(n)
    # print(f"print_{n}_0")
    # print_n_0(n)
    #print(sum_first_n(n))
    #print(factorial(n))
    print(count_digits(n))