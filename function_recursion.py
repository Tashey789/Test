def sum_of_digits(n):
    if n < 10:      #base case: if n is a single-digit number, return n
        return n
    else:           #recursion case:calculate the sum of digits
        last_digit = n % 10     #get the last digit of n
        remaining_digits = n // 10 # get the remaining digits by integer divisions with 10

        return last_digit + sum_of_digits(remaining_digits)

print(sum_of_digits(123))    