# -*- coding: utf-8 -*-


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        最长不重复的子字符串长度
        输入: "pwwkew"
        输出: 3(wke)
        :type s: str
        :rtype: int
        """
        if not s:
            return None

        char_dict, res, st = dict(), 0, 0

        for i, ch in enumerate(s):
            if ch not in char_dict or char_dict[ch] < st:
                print(res, i-st+1)
                res = max(res, i-st+1)
            else:
                st = char_dict[ch] + 1

            char_dict[ch] = i
            print(char_dict)
        return res


if __name__ == '__main__':

    s = "pwwkew"

    result = Solution().lengthOfLongestSubstring(s)

    print(result)

