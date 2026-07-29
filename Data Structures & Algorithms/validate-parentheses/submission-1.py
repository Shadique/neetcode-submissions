
# ([{}]) 
# ({[
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')' : '(', '}': '{', ']':'['}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != check[i]:
                    return False
        return not stack