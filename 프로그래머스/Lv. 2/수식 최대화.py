from itertools import permutations
import re


def solution(expression):
    
    def calc_func(expression, perm):    
        
        for cur_operator in perm:
            index = 0
            while index < len(expression):
                if expression[index] == cur_operator:
                    if cur_operator == '-':
                        result = expression[index - 1] - expression[index + 1]
                    elif cur_operator == '+':
                        result = expression[index - 1] + expression[index + 1]
                    else:
                        result = expression[index - 1] * expression[index + 1]
                        
                    expression[index - 1 : index + 2] = [result]
                    
                    index -= 1
                else:
                    index += 1

        return abs(*expression)
                    
    
    max_result = float('-inf')
    expression_list = list(map(lambda x: int(x) if x.isdigit() else x, re.findall(r'\d+|[-+*]', expression)))
    for perm in permutations('+*-', 3):
        max_result = max(calc_func(expression_list[:], perm), max_result)

    return max_result
