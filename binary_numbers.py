def binary_numbers(n):
    numbers = []
    def rec(n, i, number, zeros = 0):
        if i == n:
            if zeros <= 2:
                numbers.append(number)   
        else:
            rec(n, i + 1, number + "0", zeros + 1)
            rec(n, i + 1, number + "1", zeros)
    rec(n, 0, "")    
    return numbers        

print(binary_numbers(6))

