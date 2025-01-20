def generate_subsequences(str):
    print(str)
    if len(str) == 0:
        return [""]
    else:
        result = []
        first_char = str[0]
        subsequences = generate_subsequences(str[1:])
        for subsequence in subsequences:
            result.append(subsequence)
            result.append(first_char + subsequence)
        return result
    

print(generate_subsequences('abcd'))    
