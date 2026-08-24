class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        al = len(abbr)
        wl = len(word)

        i = j = 0
        num = 0
        while j < al:
            print(i, j, num)
            if abbr[j].isdigit():
                if num == 0 and abbr[j] == '0':
                    return False
                num = num * 10 + int(abbr[j])
                j += 1
            else:
                i += num
                num = 0
                if i >= wl or word[i] != abbr[j]:
                    return False

                i += 1
                j += 1
        return i + num == wl and j == al