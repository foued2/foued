from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        num_dict = dict()  # Create a dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                # Found a pair of indices that sum to the target
                return [num_dict[complement], i]

            # Store the number and its index in the dictionary
            num_dict[num] = i
            print(num, i, num_dict)


# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method on the instance
result = solution.twoSum([3, 2, 1, 5, 3, 4], 9)

# Print the result
print(result)


# **Two Sum Problem Using a Hash Table**
#
# The Two Sum problem involves finding a pair of numbers in an array that sum up to a specific target value.
# To efficiently solve this problem, we can use a hash table (dictionary) to keep track of the numbers
# we've encountered and their indices. Here's the process:
#
# 1. Initialize an empty hash table (dictionary) to store numbers and their indices.
#
# 2. Iterate through the list of numbers, one by one.
#
# 3. For each number, calculate its complement by subtracting it from the target value.
#
# 4. Check if the complement exists in the hash table.
#
#    - If it exists, you've found a pair of numbers that sum to the target. Return their indices.
#    - If it doesn't exist, add the current number to the hash table with its index.
#
# 5. Continue this process until you find a pair or iterate through the entire list.
#
# This approach ensures that you can quickly look up numbers and their indices,
# allowing you to find the solution in linear time complexity.
# It's a straightforward and efficient way to solve the Two Sum problems and similar problems
# that involve finding pairs of elements that satisfy certain conditions.


