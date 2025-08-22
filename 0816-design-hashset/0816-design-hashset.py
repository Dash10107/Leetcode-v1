class MyHashSet:

    def __init__(self):
        self.dic = {}

    def add(self, key: int) -> None:
        if key not in self.dic:
            self.dic[key]=1

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic[key]-=1
            if self.dic[key]==0:
                del self.dic[key]

    def contains(self, key: int) -> bool:
        return key in self.dic
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)