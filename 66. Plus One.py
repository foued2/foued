# EASY // ARRAY // MATH

from typing import List  # We are importing a list from typing module for type hinting


class Solution:  # Declaring a solution class
    @staticmethod  # This decorator allows the method to be called without instantiating the class
    def plusOne(digits: List[int]) -> List[int]:
        # A method plusOne which works with a list of integers and return
        # List of integers
        # A loop which starts from the last index of the list and iterates to the beginning of the list. This is
        # necessary because adding one must start from the rightmost digit (think about how we perform addition
        # manually).
        for i in range(len(digits) - 1, -1, -1):
            # Checking if the current digit is 9. If it is, we cannot add one without carrying over, so we set it to 0.
            if digits[i] == 9:
                digits[i] = 0
            # If the current digit is not 9, we can simply add 1 to the digit and break the loop.
            else:
                digits[i] = digits[i] + 1
                return digits  # After addition, we return the updated digits list.
        # If all digits were 9's, then digits arrays will become all zeros, and we add 1 to the left.
        return [1] + digits
