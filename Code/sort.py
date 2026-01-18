class Sort:
    def __init__(self,arr):
        self.arr = arr
    
    
    def selection_sort(self):
        sarr = self.arr
        for i in range(len(sarr)):
            min = i
            for j in range(i+1,len(sarr)):
                if arr[min] > self.arr[j]:
                    min = j
            temp = sarr[i]
            sarr[i] = sarr[min]
            sarr[min] = temp
        return sarr 
            
    
    
    
if __name__=="__main__":
    n = int(input("Enter the Size Array : "))
    arr = []
    for i in range(n):
        print(f"Enter the {i} nmumber")
        arr.append(int(input()))
    print(arr)
    sort = Sort(arr)
    print(f"Select Sort :{sort.selection_sort()}")
    