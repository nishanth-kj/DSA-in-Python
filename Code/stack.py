from multiprocessing import Value


class Stack:
    def __init__(self,n):
        self.size = n
        self.data = []
        
    def push(self,value):
        if len(self.data) <= self.size:
            print(f"Stack Pushed to the Stack{value}")
            self.data.append(value) 
        else:
            print("Stack Full")
    
    def pop(self):
        if len(self.data)<=0:
            print("Stack UnderFlow")
        else:
            self.data.pop(0)
            
    def print_stack(self):
        for i in self.data:
            if i:
                print(i)
            else:
                break
            

if __name__=="__main__":
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.pop()
    stack.push(10)
    stack.push(20)
    stack.print_stack()
    