class Solution(object):
    def twoSum(self, numbers, target):
        top = 0
        rear = len(numbers) - 1
        for i in range(len(numbers)):
            x = numbers[top] + numbers[rear]
            if(x == target):
                break
            elif(x > target):
                rear = rear - 1
            else:
                top = top + 1
        li = [top+1,rear+1]
        return li