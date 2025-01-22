# example.pyx

# Use static typing to improve performance
def sum_numbers(int n):
    cdef int i
    cdef int total = 0
    for i in range(n):
        total += i
    return total
