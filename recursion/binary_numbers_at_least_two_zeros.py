def binary_numbers(num): 
    result = []
    def rec(num, binary,i = 0, zeros=0):
        if i== num:
            if zeros <= 2:
                result.append(''.join(binary))
        else:
            binary.append("0")
            rec(num, binary, i+1, zeros+1)
            binary.pop()
            binary.append("1")
            rec(num, binary, i+1, zeros)
            binary.pop() 
    rec(num, [], 0, 0)
    return result

print(binary_numbers(8))
                 
