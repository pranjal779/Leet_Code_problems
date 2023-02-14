class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Resultant string
        result = ""
        # Indices for a and b
        aCount = len(a) - 1
        bCount = len(b) - 1
        # Carry
        carry = 0
        # Loop for all the characters in the strings
        while aCount >= 0 or bCount >= 0:
            # Sum of two bits
            totalSum = carry
            if aCount >= 0:
                totalSum += int(a[aCount])
                aCount -= 1
            if bCount >= 0:
                totalSum += int(b[bCount])
                bCount -= 1
            # Add the bit to te result
            result = str(totalSum % 2) + result
            # Modify carry
            carry = totalSum // 2
        # Final check if carry exists
        if carry > 0:
            result = str(1) + result
        return result
