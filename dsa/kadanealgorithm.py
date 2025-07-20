import sys

def largesestSubarraySum(givenNums):
    maxSum=-sys.maxsize-1
    currSum=0
    start=0
    end=0

    n=len(givenNums)
    while end <n:
        while currSum<0:
            currSum-=givenNums[start]
            start+=1

        currSum+=givenNums[end]
        end +=1

        maxSum=max(maxSum,currSum)

    return maxSum

# Function to find the maximum subarray sum
def maxSubarraySum(arr):
    
    # Stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    
    return res

def kadane(arr):
    if not arr:
        return 0  # Or handle as an error, depending on requirements

    max_so_far = arr[0]
    current_max = 0

    for num in arr:
        current_max += num
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
            
    return max_so_far

if __name__=='__main__':
    #print('Here')
    givenNums=[[1,4,-6,10,20,12],[2,3,-1,20,5],[-5,-3,-8,-9,-10],[-3,-3]]
    for arr in givenNums:
        maxsum=largesestSubarraySum(arr)
        print("method 1",maxsum)
        #print('*'*20)
        maxsum=maxSubarraySum(arr)
        print('method 2',maxsum)
        #print('*'*20)
        maxsum=kadane(arr)
        print('method 3',maxsum)
        #print('*'*20)
    
