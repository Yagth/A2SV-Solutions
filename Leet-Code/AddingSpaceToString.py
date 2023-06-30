class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ss = ""
        offset = 0
        for i in spaces:
            ss += s[offset:i] + " "
            offset = i
        ss += s[offset:]
        return ss
