#Check if a number is positive, negative, or zero
def check_number_positive_negative_zero(number):
    if number == 0:
        print(f"Number is : {number}")
    
    elif number < 0:
        print(f"Number is Negative : {number}")

    elif number > 0:
        print(f"Number is Positive : {number}")

    else:
        print(f"Invaild :{number}")

#Check if a number is even or odd
def check_even_odd(n):
    if n%2==0:
        print(f"{n} is even")
    elif n%2!=0:
        print(f"{n} is odd")
    else:
        print("Invaild")


if __name__ == "__main__":
    try:   
        n = int(input(("Enter the number : ")))
        check_number_positive_negative_zero(n)
        check_even_odd(n)
    except Exception as e:
        print(f"Error Processing : {e}")

