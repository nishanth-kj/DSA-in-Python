class Hashing:
    def __init__(self,arr):
        self.arr = arr
    
    
    def frequency(self):
        freq = {}
        for i in self.arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1
        print(freq)
    
if __name__=="__main__":
    arr = []
    n = int(input("Enter the Size of the list"))
    for i in range(n):
        val = None
        val = input("Enter the value")
        arr.append(val)
    hashing = Hashing(arr)
    hashing.frequency()