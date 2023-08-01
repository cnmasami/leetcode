# 设计哈希集合

# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#
# 实现 MyHashSet 类：
#
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#


class MyHashSet:

    def __init__(self):
        self.hash = set()

    def add(self, key: int) -> None:
        self.hash.add(key)

    def remove(self, key: int) -> None:
        self.hash.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return True
        else:
            return False


#  分桶
class MyHashSetBucket:
    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key):
        hash_key = self.hash(key)
        if not self.table[hash_key]:
            self.table[hash_key] = [0] * self.itemsPerBucket
        self.table[hash_key][self.pos(key)] = 1

    def remove(self, key):
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        hashkey = self.hash(key)
        return (self.table[hashkey][self.pos(key)] != []) and (self.table[hashkey][self.pos(key)] == 1)


class MyHashSetBucket2:
    def __init__(self):
        # 1009是因为1000以上的第一个质数，最坏状态下拉不到1000长度链表
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]
