import math

def solution(arrayA, arrayB):
    
    def check_max_num(gcd_arr, check_arr):
        cur_gcd = gcd_arr[0]
        for item in gcd_arr[1:]:
            cur_gcd = math.gcd(cur_gcd, item)
        
        if all(item % cur_gcd != 0 for item in check_arr):
            return cur_gcd
        return 0
    
    
    result_A = check_max_num(arrayA, arrayB)
    result_B = check_max_num(arrayB, arrayA)
    
    return max(result_A, result_B)
