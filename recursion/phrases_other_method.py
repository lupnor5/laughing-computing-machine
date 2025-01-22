def phrases(arr, i = 0):
    if i== len(arr):
        return ['']
    else:
        fromNext = phrases(arr, i+1)
        output = []
        for word in arr[i]:
            for phrase in fromNext:
                output.append(word + (' ' if len(phrase) > 0 else '') + phrase)
        return output        
    

print(phrases(
    [['I','You','They'],
    ['love','hate'],
    ['food','games']]))


