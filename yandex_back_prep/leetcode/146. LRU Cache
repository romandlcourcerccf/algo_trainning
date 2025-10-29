class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.deque = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.deque.append(key)
        return self.cache.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        print(f'Put key {key} value {value}')
        if key in self.cache:
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.deque.append((key, value))

            if len(self.deque) > self.capacity:
                 lk, lv = self.deque.pop()
                 del self.cache[lk]
       
        print('Cache after : ')
        print(self.cache)
        print(self.deque)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)