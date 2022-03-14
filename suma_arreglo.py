class vectorSum():
    def __init__(self,arr):
        self.arr = arr
        self.array_sum = self.array_addition()
        
    def array_addition(self):
        addition = 0
        for i in self.arr:
            addition += i
        return addition
    
vec = vectorSum([1,2,3,3,5,7,2])
print(f"La suma del vector es: {vec.array_sum}")