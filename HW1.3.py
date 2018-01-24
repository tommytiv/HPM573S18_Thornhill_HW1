# HPM 573 Advanced Topics in Modeling Health Care Decisions Spring 2018 #
# Tommy Thornhill #
# Assignment: HW1.3#

def sum_iteration(n):
#     Input: n, a positive integer
#     Returns: sum of all numbers from 1 to n
    x = 0
    i = 1
    while i <= n:
        x = x+i
        i = i + 1
    return x
print (sum_iteration(100))


def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)
print (sum_recursive(100))
