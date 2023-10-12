# Roman to Integer - LeetCode

| category               | difficulty |
| ---------------------- | ---------- |
| Hash Table Math String |            |

[link](https://leetcode.com/problems/roman-to-integer/description)

## Description

Can you solve this real interview question? Roman to Integer - Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Note

'''  
I can be placed before V (5) and X (10) to make 4 and 9.  
 X can be placed before L (50) and C (100) to make 40 and 90.  
 C can be placed before D (500) and M (1000) to make 400 and 900.  
'''

1. 윗 부분을 보고 감이 잡혔다.
2. 일단 I, V, X, L, C, D, M... 각자의 값이 있는데 if문으로 해당 문자가 맞으면 그 값에 맞도록 `result`에 더해준다.
3. 그리고 `V` 앞이나, `X` 앞에 `I`가 붙게 되면 각각 4 또는 9가 해당된다. 그런데 기존에 `I`값이 들어가 있다면 3 또는 8을 더해주기만 하면 된다.
4. 다른 것들도 일맥상통하다. 그래서 이러한 결과가 나왔다.
