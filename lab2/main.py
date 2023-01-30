
def calculate(s):
        arr = []
        for c in s:
            arr.append(c)
        return helper(arr)

def helper(s):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = num*10+int(c)
            if c == '(':
                num = helper(s)
            if len(s) == 0 or (c == '+' or c == '-' or c == '*' or c == '/' or c == ')'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
                if sign == ')':
                    break
        return sum(stack)

def check(string):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:    
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]  
            else: return False  
    return (not stack)

str=input("Введите строку ")
if check(str) :
    if str[len(str)-1] == "=":
        try: print(calculate(str[:-1]))
        except: print("Не пройдена проверка на дурака")

    else: 
        print("В выражении отсутствует знак =")
else : 
    print("Проблема со скобками")
