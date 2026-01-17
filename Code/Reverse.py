class Solution:

    def rev(n):
        revNum = 0

        while n > 0:
            lastDigit = n % 10

            revNum = revNum * 10 + lastDigit

            n = n // 10

        return revNum

    def rrev(self,n):
        if n < 10:
            return n
        digit = 
        return self.rrev(n//10)
    
    def swap(a,b):
        return 



    
if __name__=="__main__":

    obj = Solution

    #print(obj.rev(1232345))
    print(obj.rrev(123456))



