class Trie(object):

    def __init__(self):
        self.inse = set()
        self.star = set()

    def insert(self, word):
        self.inse.add(word)
        for i in range(len(word)):
            self.star.add(word[0:len(word)-1-i])

    def search(self, word):
        if word in self.inse:
            return True
        

    def startsWith(self, prefix):
        if (prefix in self.star) or (prefix in self.inse):
            return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)