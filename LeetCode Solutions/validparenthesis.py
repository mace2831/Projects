class Solution:
    def isValid(self, s: str) -> bool:
        #Create a dictionary of opening brackets and their counterparts
        paren = {'(':')','[':']','{':'}'}
        #create empty stack
        stack = []
        #iterate through the input string
        for char in s:
            #if the current character is an opening bracket then add it to the stack
            if char in '([{':
                stack.append(char)
            #if the current character is not an opening bracket check if the stack is
            #empty or if the current character is not the corresponding closing bracket
            #then return false
            elif len(stack) == 0 or char != paren[stack.pop()]:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('()'))
    print(sol.isValid('(]'))
    print(sol.isValid('([])'))
