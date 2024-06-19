class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st= Stack()
        for x in s:
            if x != '*':
                st.push(x)
            else:
                st.pop()
        s=st.display()
        print(s)
        return "".join(s)

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
    def display(self):
        print(self.stack)
        return self.stack