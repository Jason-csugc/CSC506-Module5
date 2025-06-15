# hash.py

class Hash(object):
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]

    def hashFunction(self, key):
        return (key % self.__bucket)
    
    def insertItem(self, key):
        index = self.hashFunction(key)
        self.__table[index].append(key)

    def deleteItem(self, key):
        index = self.hashFunction(key)

        if key not in self.__table[index]:
            return
        
        self.__table[index].remove(key)

    def displayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end='')
            for x in self.__table[i]:
                print(" --> %d" % x, end='')
            print()
