# 34. Find First and Last Position of Element in Sorted Array

| category             | difficulty |
| -------------------- | ---------- |
| array, binary search | medium     |

[link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

## Description

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

_You must write an algorithm with O(log n) runtime complexity._

## Note

- Arrays sorted in ascending order
- O(log n)

### 첫번째 문제 풀이 (실패)

1. 먼저 `find`와 `rfind`라는 문자열 클래스의 메서드를 알고 있었기 때문에 문제를 `find`와 `rfind`로 풀고자 했다.
2. 그러나 해당문제를 문자열 메서드로 풀려고 할 시, 에러가 발생한다. `nums`의 아이템 중 10의 자리수의 값에서 만약 0을 찾고자 했을 때, `0, 0, 0, 1` 라고 했을 때 값은 `[0, 2]` 가 나오면 되지만, `0, 0, 0, 0, 10`과 같은 배열이 나오게 된다면 `[0, 5]` 라는 답이 나온다. 그냥 10의 자리의 수가 나오면 문제가 발생한다.

### 두번째 문제 풀이 (마음에 안듦)

1. `target`의 값중 **첫 index**를 찾는데에는 문제가 없다. 이미 만들어진 메소드를 사용하면 되기 때문이다.
2. 그리고 `target`의 **마지막 index**를 찾는데에 어려웠다. 솔직히 어렵지 않는데 하도 안했어서 머리가 잘 안돌아갔다. 어떻게 풀릴지는 보였지만 시간이 걸렸다.
3. 이진 탐색으로 기준과 같다면 일단 `result`값을 `mid`와 같이 한다. 그리고 마지막 값을 찾는 경우 밖에 없으므로 `left = mid + 1`으로 범위를 조였다.
4. 기준이 `target`보다 크다면 `right`값을 줄여서 범위를 조일 수 있다.
5. 기준이 `target`보다 작다면 `left`값을 높여 범위를 조일 수 있는데 이 경우는 없다. (위 `searchRange`에서 **첫 index**를 찾았기 때문)
   해당 풀이는 너무 난잡하기 때문에 수정하기로 마음먹었다.

### 세번째 문제 풀이 (성공)

1. 두번째 문제 풀이와 로직은 똑같다. **첫 index**와 **마지막 index**를 찾는 데 같은 메서드를 쓴다는 점이 다르다. (bool값을 넣고 **첫 index**를 찾을 지 **마지막 index**를 찾을지 나눌 수 있음)
2. 사실 두번째의 방식이 runtime이 조금 더 빠를 수 있지만(가능성) 코드가 깨끗한지로 보았을 때 세번째 풀이가 더 좋은 것 같다.
