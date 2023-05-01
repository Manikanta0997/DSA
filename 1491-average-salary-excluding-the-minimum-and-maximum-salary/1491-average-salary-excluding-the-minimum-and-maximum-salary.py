class Solution(object):
    def average(self, salary):
        ma = max(salary)
        mi = min(salary)
        x = sum(salary)
        x = x - ma - mi
        x = float(format(x,'.5f'))
        x = x / (len(salary)-2)
        return x
        
        