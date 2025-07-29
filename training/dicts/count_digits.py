def is_permut(x, y):

    def count_digits(num):
        d_count = [0]*10
        while num > 0:
            last = num % 10
            d_count[last] +=1
            num //=10
        return d_count
    

    c_x = count_digits(x)
    c_y = count_digits(y)


    for d in range(10):
        if c_x[d] != c_y[d]:
            return False
        
    return True

assert is_permut(101, 110) == True
assert is_permut(111, 110) == False
