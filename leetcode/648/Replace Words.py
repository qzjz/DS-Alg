#!/usr/bin/python3
"""Replace words
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
    1. The input will only have lower-case letters.
    2. 1 <= dict words number <= 1000
    3. 1 <= sentence words number <= 1000
    4. 1 <= root length <= 100
    5. 1 <= sentence words length <= 1000
"""


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str

        Examples:

            >>> s = Solution()
            >>> dict = ["cat", "bat", "rat"]
            >>> sentence = "the cattle was rattled by the battery"
            >>> s.replaceWords(dict, sentence)
            'the cat was rat by the bat'
        """
        dict.sort(key=len)
        word_array = sentence.split(' ')
        for root in dict:
            for i in range(len(word_array)):
                if word_array[i].startswith(root):
                    word_array[i] = root
        return ' '.join(word_array)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
