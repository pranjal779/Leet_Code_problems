class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits (1s) in num1 and num2
        bit_count_num1 = num1.bit_count()
        bit_count_num2 = num2.bit_count()

        # If num1 has more set bits than num2, we need to decrease the number of set bits in num1
        while bit_count_num1 > bit_count_num2:
            # Remove the rightmost set bit from num1 using (num1 & num1 - 1)
            num1 &= num1 - 1
            # Decrement the counter for the number of set bits in num1
            bit_count_num1 -= 1

        # If num1 has fewer set bits than num2, we need to increase the number of set bits in num1
        while bit_count_num1 < bit_count_num2:
            # Get the number that is the smallest power of two greater than num1, which doesn't have a set bit in common with num1
            number_to_or = num1 + 1
            while num1 & number_to_or:
                number_to_or = number_to_or << 1
              
            # Add this number to num1 (same as ORing it with num1)
            num1 |= number_to_or
            # Increment the counter for the number of set bits in num1
            bit_count_num1 += 1

        # Return the modified num1 which has the same number of set bits as num2
        return num1
        
