# n-Day FIRST ATTEMPT
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if not (key in self.cache):
            return -1

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        print(self.order)

        if len(self.cache) > self.capacity:
            least_used = self.order[0]
            del self.cache[least_used]

            self.order = [key for key in self.order if key != least_used]
"""

# SECOND ATTEMPT
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        # cache에 없으면 -1
        if not (key in self.cache):
            return -1

        self.record(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        self.record(key)

        if len(self.cache) > self.capacity:
            least_used = self.order[0]
            del self.cache[least_used]

            self.order.remove(least_used)

    # 새로운 순서로 갱신
    def record(self, key):
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
"""

# REFERENCE ATTEMPT
from collections import OrderedDict


class LRUCache:
    __slots__ = ("data", "capacity")

    def __init__(self, capacity: int):
        self.data: dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return (
            -1
            if key not in self.data
            else self.data.setdefault(key, self.data.pop(key))
        )

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
