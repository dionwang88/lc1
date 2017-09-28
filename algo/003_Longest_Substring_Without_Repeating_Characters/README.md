###3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Analysis

This problem can use two pointer to generate a scan window. Using a hashmap to save the distinct Characters,
when encounter a duplicated one, slide the previous pointer to the duplicated position, and drop the characters before this position.
