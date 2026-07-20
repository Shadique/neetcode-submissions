class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + i + 'ñ'
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        cur = ""
        for c in s:
            if c == 'ñ':
                result.append(cur)
                cur = ""
            else:
                cur += c
        return result
