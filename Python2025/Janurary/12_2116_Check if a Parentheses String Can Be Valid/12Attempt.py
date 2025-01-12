class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # The length of the string s.
        string_length = len(s)
      
        # A valid string must have an even number of characters.
        if string_length % 2 != 0:
            return False

        # Counter for unbalanced open parentheses.
        balance = 0
      
        # First pass to check if we can balance from left to right.
        for index in range(string_length):
            # If we encounter an open parenthesis or an unlocked character, we increment balance.
            if s[index] == '(' or locked[index] == '0':
                balance += 1
            # If we can match an open parenthesis, we decrement balance.
            elif balance:
                balance -= 1
            # If balance is 0 and we encounter a closed parenthesis that is locked, it is unbalanced and can't be valid.
            else:
                return False
      
        # If after the first pass, we have managed to match every parenthesis, the string may be valid.
        # However, we need to check the same from right to left.
      
        # Reset balance for the second pass.
        balance = 0
      
        # Second pass to check if we can balance from right to left.
        for index in range(string_length - 1, -1, -1):
            # If we encounter a closed parenthesis or an unlocked character, we increment balance.
            if s[index] == ')' or locked[index] == '0':
                balance += 1
            # If we can match a closed parenthesis, we decrement balance.
            elif balance:
                balance -= 1
            # If balance is 0 and we encounter an open parenthesis that is locked, it is unbalanced and can't be valid.
            else:
                return False
      
        # If both passes are successful, the string is valid.
        return True
        
