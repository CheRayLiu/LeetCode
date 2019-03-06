"""
Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_stack = []
        cur_encode = ""
        
        for char in s:
            if char != "]":
                char_stack.append(str(char))
            else:
                while char_stack[-1] != "[":
                    cur_encode = char_stack.pop() + cur_encode
                char_stack.pop()
                multi = ""
                while char_stack and char_stack[-1].isdigit():
                    multi = char_stack.pop() + multi
                char_stack.append(int(multi)*cur_encode)
                cur_encode = ""
        decode_str = ""
        for decode_sub_str in char_stack:
            decode_str += decode_sub_str
        return decode_str