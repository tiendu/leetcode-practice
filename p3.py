def lengthOfLongestSubstring(s: str) -> int:
    char_idx = {}  # Dictionary to store the most recent index of each character
    left = 0  # Left pointer of the sliding window
    max_len = 0  # Result to store the maximum window length without repeating characters

    for right, char in enumerate(s):  # Right pointer moves through each character
        # If character has been seen before and is within the current window
        if char in char_idx and char_idx[char] >= left:
            # Move the left pointer to one past the last occurrence of the current character
            left = char_idx[char] + 1

        # Update the latest index of the character
        char_idx[char] = right

        # Update the maximum length found so far
        max_len = max(max_len, right - left + 1)

    return max_len
