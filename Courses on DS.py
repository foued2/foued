class Solution(object):
    @staticmethod
    def merge(nums1, m, nums2, n):
        i = 0
        j = 0
        k = 0
        expected_nums = [0] * (m + n)

        while k < m + n:
            if i < m and (j >= n or nums1[i] < nums2[j]):
                expected_nums[k] = nums1[i]
                i += 1
            elif j < n and (i >= m or nums1[i] >= nums2[j]):
                expected_nums[k] = nums2[j]
                j += 1
            k += 1
        median = expected_nums[(m + n) // 2]
        return expected_nums, median


# Call the merge() method with two lists [1, 2, 3, 8, 10, 20] and [2, 5, 6], and their lengths 6 and 3 respectively.
print(Solution.merge([1, 2, 3, 8, 10, 20], 6, [2, 5, 6], 3))
print((6 + 3) // 2)

from itertools import combinations

numbers = [-1, 0, 1, 2, -1, -4]
result = list(combinations(numbers, 2))

print(len(result))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


original_list = [-1, 0, 1, 2, -1, -4]

sorted_list = quicksort(original_list)
print(sorted_list)
s = [1, 0, -1, 0, -2, 2] + [2]
print(s)
print([1, 2, 1][2:3])


def find_next_bigger(arr):
    result = [next((num for num in arr[i + 1:] if num > arr[i]), None) for i in range(len(arr))]
    return result


# Example usage:
my_array = [3, 7, 1, 5, 2, 8, 4]
result_array = find_next_bigger(my_array)
print(result_array)


def count_d(input):
    return input.count("D") + input.count("d")


print(count_d("Debris was scattered all over the yard."))

