class CustomStack(object):

    def __init__(self, maxSize):
        self.li = []
        for i in range(maxSize):
            self.li.append(-1)
        self.top = 0
        self.maxsize = maxSize

    def push(self, x):
        if(self.maxsize > self.top):
            self.li[self.top] = x
            self.top = self.top + 1

    def pop(self):
        if(self.top > 0):
            self.top = self.top - 1
            return self.li[self.top]
        else:
            return -1
        

    def increment(self, k, val):
        if(k > self.top):
            k = self.top
        for i in range(k):
            self.li[i] = self.li[i] + val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)