from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}  # Dictionary to store value -> index mapping

    for i, v in enumerate(nums):
        remaining = target - v  # The number we need to find
        if remaining in seen:
            return [seen[remaining], i]  # Found the two numbers
        seen[v] = i  # Store the current number with its index

    return []  # Should never reach here if solution exists

