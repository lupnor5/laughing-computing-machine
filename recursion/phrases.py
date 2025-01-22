def rec(arr, i, phrase, output): 
    if i == len(arr):
        output.append(' '.join(phrase))
    else: 
        for word in arr[i]:
            phrase.append(word)
            rec(arr, i+1, phrase, output)
            phrase.pop()

def phrases(arr):
    output=[]
    rec(arr, 0, [], output)
    return output                


print(phrases(
    [['I','You','They'],
    ['love','hate'],
    ['food','games']]))



