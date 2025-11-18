from typing import Final
class Pattern:
    def __init__(self,n):
        self.n:Final[int] = n

    def pattern1(self):
        """
        ***
        ***
        ***
        """
        n = self.n
        print("*"*n)

    def pattern2(self):
        """
        *
        **
        ***
        ****
        """
        n = self.n
        for i in range(1,n+1):
            print("*"*i)


    def pattern3(self):
        """
        1
        12
        123
        1234
        """
        n = self.n
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()

    def pattern4(self):
        """
        1
        22
        333
        4444
        55555    
        """
        n = self.n
        for i in range(1,n+1):
            print(f"{i}"*i)
    
    def pattern5(self):
        """
        ****
        ***
        **
        *
        """
        n = self.n
        for i in range(n,0,-1):
            print(f"*"*i)

    def pattern6(self):
        """
        12345
        1234
        123
        12
        1
        """
        for i in range(n+1,0,-1):
            for j in range(1,i):
                print(f"{j}", end="")
            print()

    def pattern7(self):
        """
            *
           ***
          *****
         *******
        """
        n = self.n
        for i in range(n):
            print(" " * (n - i - 1), end="")
            print("*" * (2 * i + 1))            

    def pattern8(self):
        """
          *******
           *****
            ***
             *
        """
        n = self.n
        for i in range(n-1,-1,-1):
            print(" " * (n - i - 1), end="")
            print("*" * (2 * i + 1))   

    def pattern9(self):
        """
               *
              ***
             *****
            *******
            *******
             *****
              ***
               *
        
        """
        for i in range(n):
            print(" " * (n - i - 1), end="")
            print("*" * (2 * i + 1))    
        for i in range(n-1,-1,-1):
            print(" " * (n - i - 1), end="")
            print("*" * (2 * i + 1)) 
                

    




if __name__ == "__main__":
    try:
        n = int(input("Enter the Number : "))
    except Exception as e:
        print(f"{e}")
        n = 5
        print(f"N Assigned to : {n}")
        pass


    p = Pattern(n)
    #p.pattern1()
    #p.pattern2()
    #p.pattern3()
    #p.pattern4()
    #p.pattern5()
    #p.pattern6()
    #p.pattern7()
    #p.pattern8()
    p.pattern9()