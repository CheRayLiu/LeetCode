class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        char_stack = []
        op = ("+","-","*","/")
        for char in tokens:
            if char in op:
                right = int(char_stack.pop())
                left = int(char_stack.pop())
                if char == "+":
                    char_stack.append(str(left+right))
                elif char == "-":
                    char_stack.append(str(left-right))
                elif char == "/":
                    if ( left*right < 0 and left%right != 0):
                        char_stack.append(str(left//right+1))
                    else: 
                        char_stack.append(str(left//right))
                elif char == "*":
                    char_stack.append(str(left*right))
            else:
                char_stack.append(char)        
        return int(char_stack[0])