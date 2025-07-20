#from kadanealgorithm import kadane
def getbits(char):
    if char=='0':
        return 1
    return -1

def kadane(arr):
    ans=0
    if not arr:
        return 0  # Or handle as an error, depending on requirements
    for i in arr:
        if i=="1":
            ans+=1
    new_arr=[getbits(x) for x in arr]
    #print(new_arr)
    max_so_far = new_arr[0]
    current_max = 0

    for num in new_arr:
        current_max += num
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
            
    return ans + max_so_far

givenNums="0001000"
print(kadane(givenNums))
        