

### sliding window


# k = 3
# arr = [ 1, 2, 3, 4, 5, 6 ]

# ### get sum of all subarrays length k
# results = []

# for i in range(0, len(arr) -k +1):
    
#     sum = 0
#     if i == 0:
#         for j in range(i, i+k):
#             sum += arr[j]
#         results.append(sum)
#     else: 
#         sum = results[-1] -i + i+k
#         results.append(sum)

# print(results)





### slding window #2

# x = 7
# arr = [1, 2, 3, 4, 5, 6]


# min_length = float('inf')


# start = 0
# end = 0
# curr_sum = 0


# while end < len(arr):
#     curr_sum += arr[end]
#     end += 1
#     print(f"start {start}, end {end}")
    
#     while start < end and curr_sum >= x:
#         curr_sum -= arr[start]
#         start += 1
    
#         min_length = min(min_length, end - start + 1)

# min_length






### sliding window stock price 

prices = [7,1,5,3,6,4]

class Solution(object):
    def maxProfit(self, prices):
        
        start = 0
        end = 0
        max_profit = 0
        
        while end < len(prices):
            
            if prices[end] < prices[start]:
                start = end
            
            max_profit = max(max_profit, prices[end] - prices[start])
            
            
            end += 1
        
        return max_profit
s = Solution()
print(s.maxProfit(prices))

        