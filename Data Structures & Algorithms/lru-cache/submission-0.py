class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val
            return val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        elif len(self.dict)<self.capacity:
            self.dict[key] = value
        else:
            key1 = list(self.dict)[0]
            del self.dict[key1]
            self.dict[key] = value
        
