# Zigzag Conversion - LeetCode

| category | difficulty |
| -------- | ---------- |
| String   | Medium     |

[link](https://leetcode.com/problems/zigzag-conversion/description)

## Description

Can you solve this real interview question? Zigzag Conversion - The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P A H N
A P L S I I G
Y I R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P I N
A L S I G
Y A H R
P I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

## Note

문제를 푼 방법

- 일단 행을 하나씩 늘려가면서 테스트케이스를 가지고 그림을 그리면서 `output`이 어떻게 나와야하는지 이해를 먼저 했다.
- `Explanation`을 보고 이해를 했다.

1. 일단 `input`으로 문자열 `s`, 행의 갯수 `numRows`가 주어졌다.
2. 정답들은 행순서대로 값이 찍힌 값이 출력되게하면 되었다.
3. 그러면 행 갯수 만큼 배열을 만들고, 배열에 가장 첫 번째 값을 빼서 해당행 배열에 넣는다.
4. 그리고 다음 행배열에다가 그다음 값을 넣는다. 반복을 한다.
5. 마지막 행이라면 다시 이전행배열에 값을 넣는다.
6. 문자열 s가 길이가 0라면 반복을 종료하고, 행순서대로 행배열의 문자열을 join하면 값이 나온다.
