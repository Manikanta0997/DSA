class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            for j in range(len(image)/2):
                temp = image[i][j]
                image[i][j] = image[i][len(image)-j-1]
                image[i][len(image)-j-1] = temp
        for i in range(len(image)):
            for j in range(len(image)):
                if(image[i][j] == 0):
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
                
            