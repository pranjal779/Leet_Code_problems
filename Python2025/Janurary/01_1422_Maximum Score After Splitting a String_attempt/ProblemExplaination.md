Solution
Approach 1: Brute Force
Intuition

In this problem, we need to make a "split" which involves separating the input into a left part and a right part.

To start, we can check every possible split. We will use an integer i to iterate over the string, where i represents the index of the final character in the left part.

For a given i, we iterate on the indices of s from 0 to i and count how many times 0 occurs. We then iterate on the indices from i + 1 until the last index and count how many times 1 occurs.
The sum of these counts represents the score for the current split, and we take the maximum of all scores.

Note that we cannot iterate i until the final index, but rather the second last index. If we were to iterate to the final index, the right part would be empty, which is not allowed by the problem.

Algorithm

Initialize the answer ans = 0.
Iterate i from 0 until s.length - 1:
Initialize the current score curr = 0.
Iterate j from 0 to i:
If s[j] == '0', increment curr.
Iterate j from i + 1 until s.length:
If s[j] == '1', increment curr.
Update ans with curr if it is larger.
Return ans.
Implementation

```py

class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s) - 1):
            curr = 0
            for j in range(i + 1):
                if s[j] == "0":
                    curr += 1
            
            for j in range(i + 1, len(s)):
                if s[j] == "1":
                    curr += 1
            
            ans = max(ans, curr)
    
        return ans
```

Complexity Analysis

Given n as the length of nums,

Time complexity: O(n^2)

We iterate i over n−1 indices. For each iteration, we have two iterations over j, traversing over a total of n indices. Thus, we iterate O(n⋅(n−1))=O(n^2) times.

Space complexity: O(1)

We aren't using any extra space other than a few integers.


Approach 2: Count Left Zeros and Right Ones
Intuition

We can improve on the previous solution by noticing that between a split at index i and index i + 1, we are only changing one character
(more specifically, moving it from the right substring to the left substring), leaving the other characters unchanged.
Instead of iterating over the entire string for each split, we only need to check the moved character and calculate the score for the new split based on the previous split.

We start by counting how many times 1 occurs in s. Let's store this value in a variable ones. 
We will also have a variable zeros that represents how many 0 are in the left part.
Initially, our variables ones and zeros are set as if the left part is empty and the right part is the entire string.

Now, we iterate i in the same manner as the previous approach: each index i represents the final index of the left part.
At each iteration i, we remove s[i] from the right part and add it to the left part.
![1](https://github.com/user-attachments/assets/6c5a0ddb-5920-4e58-9611-4647a7008150)

example:

There are two possibilities for each index i:

If s[i] == '1': this 1 was in the right part, but it is now joining the left part. Thus, we lose 1 score since the right part is losing a 1. Decrement ones.
If s[i] == '0', this 0 was in the right part, but it is now joining the left part. Thus, we gain 1 score since the left part is gaining a 0. Increment zeros.
We update the answer with zeros + ones at each iteration if it is larger.

Algorithm

Initialize ones as the number of times 1 occurs in s.
Initialize zeros = 0 and the answer ans = 0.
Iterate i from 0 until s.length - 1:
If s[i] == '1', decrement ones.
Otherwise, increment zeros.
Update ans with zeros + ones if it is larger.
Return ans.
Implementation

```py
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0 

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
        
            ans = max(ans, zeros + ones)
        
        return ans
```

Complexity Analysis

Given n as the length of nums,

Time complexity: O(n)

We start by finding the frequency of 1, which costs O(n). Next, we iterate over the string once, performing O(1) work at each iteration. Thus, our time complexity is O(2n)=O(n).

Space complexity: O(1)

We aren't using any extra space other than a few integers.


Approach 3: One Pass
Intuition

![image](https://github.com/user-attachments/assets/42e5176b-b160-4170-9463-174420b50d44)
![image](https://github.com/user-attachments/assets/6b1a5524-a290-4078-a64d-e84bb153ce33)
![image](https://github.com/user-attachments/assets/04550e0d-0ee6-43e1-ade0-6d6895d5547f)


Algorithm

Initialize ones = 0, zeros = 0, and best to a very small value like negative infinity.
Iterate i from 0 until s.length - 1:
If s[i] == '1', increment ones.
Otherwise, increment zeros.
Update best with zeros - ones if it is larger.
If the final character of s is equal to '1', increment ones.
Return best + ones.
Implementation
```py
class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            best = max(best, zeros - ones)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones
```

Complexity Analysis

Given n as the length of nums,

Time complexity: O(n)

We make one pass over nums, performing O(1) work at each iteration.

Space complexity: O(1)

We aren't using any extra space other than a few integers.
