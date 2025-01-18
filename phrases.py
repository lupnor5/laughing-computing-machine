"""def test(): 
    sample = ['I', 'You', 'They']
    print (sample[0:])
    print (sample[1:])
    print (sample[2:])


test()    

"""

def phrases(arr, i=0, j=0):
    n = len(arr)
    m = len(arr[1])

    #print(f"{n}x{m}")

    if j > n-1: 
        return ""
    elif i > m-1:
        return ""
    else: 
        for j in range(0, n):
            result = result + arr[j][i] + " " + phrases(arr, i + 1)
        print(f"result {result}")
        return result
    


print(phrases(
    [['I','You','They'],
    ['love','hate'],
    ['food','games']]))

