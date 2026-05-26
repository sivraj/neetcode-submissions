class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = f"{encoded}{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            l = i
            word_len = ''
            while s[l] != '#':
                word_len += s[l]
                l += 1
            start = l+1
            end = start + int(word_len)
            words.append(s[start:end])

            i = end
        return words

