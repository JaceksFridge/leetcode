

### sliding window


k = 3
arr = [ 1, 2, 3, 4, 5, 6 ]

### get sum of all subarrays length k
results = []

for i in range(0, len(arr) -k +1):
    
    sum = 0
    if i == 0:
        for j in range(i, i+k):
            sum += arr[j]
        results.append(sum)
    else: 
        sum = results[-1] -i + i+k
        results.append(sum)

print(results)