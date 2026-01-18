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

def print_name_n(n,name):
    if n > 0:
        print(name)
        print_name_n(n-1,name)
        
def rev_arr(arr):
    def helper(arr,l,r):
        if l >= r :
            return arr
        arr[l], arr[r] = arr[r] , arr[l] 
        return helper(arr, l+1, r-1)
    return helper(arr,0,len(arr)-1) 
    
def str_pal(str):
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    return rev_str == str
    
def fib(n,a=0,b=1):
    if n == 0:
        return n
    print(a,end=" ")
    return fib(n-1,b,a+b)
        
    
    
        
if __name__=="__main__":
    # print("Hello")
    #n = int(input("Enter the number "))
    # print(f"print_0_{n}")
    # print_0_n(n)
    # print(f"print_{n}_0")
    # print_n_0(n)
    #print(sum_first_n(n))
    #print(factorial(n))
    #print(count_digits(n))
    #print_name_n(n,input("Enter the Text to Print"))
    #arr = [1,2,3,4,5]
    #print(rev_arr(arr))
    #print(str_pal("ABA"))
    print(fib(5))
    