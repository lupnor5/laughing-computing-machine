def from_string_to_dictionary():
    dic_str = "0: +, 1: . , 2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ"
    dic_arr =  dic_str.replace(" ", "").split(',')
    dict = {}
    for item in dic_arr:
        dicEntry = item.split(":")
        dict[dicEntry[0]] = list(dicEntry[1])
    return dict

def rec(char_matrix, i, phrase, output): 
    if i == len(char_matrix):
        output.append(''.join(phrase))
    else:
        for item in char_matrix[i]:
            phrase.append(item)
            rec(char_matrix, i+1, phrase, output)
            phrase.pop()

def find_chars_to_combine(str):
    dict = from_string_to_dictionary() 
    input_arr = list(str)
    char_matrix = []
    for key in input_arr:
        char_matrix.append(dict[key]) 
    return char_matrix

def keypad_combinations(str):
    char_matrix = find_chars_to_combine(str)
    output = []
    rec(char_matrix, 0, [], output)
    return output    

print(
    keypad_combinations("374")
)

