# LRU Cache - LeetCode

| category                                         | difficulty |
| ------------------------------------------------ | ---------- |
| Hash Table Linked List Design Doubly-Linked List | Medium     |

[link](https://leetcode.com/problems/lru-cache/description)

## Description

Can you solve this real interview question? LRU Cache - Design a data structure that follows the constraints of a Least Recently Used (LRU) cache [https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU].

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4

Constraints:

- 1 <= capacity <= 3000
- 0 <= key <= 104
- 0 <= value <= 105
- At most 2 \* 105 calls will be made to get and put.

## Note

1, 2번의 문제풀이는 넘기겠다. 그냥 풀었기 때문에

### 3번 문제 풀이

1. `OrderDict`라는 컬렉션을 사용하여 구현을 했다.
2. pop 메서드도 같이 사용하면서 `setdefault` 메서드를 사용해서 기존 중복되는 키가 있으면 제거해서 순서를 할당하게 하는 방법
3. `move_to_end` 라는 메서드가 있는데 이는 기존에 키가 있으면 가장 순서가장 앞으로 오게 하고, 그 다음 업데이트 시킨다.
4. 이 과정에서 `KeyError`가 발생했으면, 기존 키가 없으므로 할당시킨다. 새로운 값이 할당되면 `capacity`를 생각해야 하므로, 지정된 `capacity`를 넘기면 가장 앞 순서의 `item`을 삭제시킨다.

다른 사람의 풀이를 보고 느낀 점이 있다.
collection을 잘 사용한다면, 문제 풀이가 쉬워지고 내가 짠 코드보다 빠른 경우가 많다.
여러 문제를 풀어보면서 익히면 좋을 것 같다는 생각이 들었다.
