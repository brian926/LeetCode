# 121. Best Time to Buy and Sell Stock

## **The Problem**
You are given an array *prices* where *prices[i]* is the price of a given stock on the *ith* day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### **Examples**
Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```
**Example 2**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## **The Solution**
For this, we'll use a sliding window that will change if we find a new low price and a new max price.
We start in the beginning of the array with our left pointer, while our right pointer will start at index 1 and traverse through the array. Then, comparing the left and right point we check if the right point is less than the left and if so we assign our left pointer to our right as this is now the new lowest day. Lastly, we give our result value the max of either itself or the difference of the two pointers.
Our left pointer is the day we bought stock while our right pointer travels through finding the max profit.


## **The Code**

```python
def maxProfit(self, prices: List[int]) -> int:
    res, l = 0, 0
    
    # [7, 1, 5, 3, 6, 4]
    for r in range(1, len(prices)):
        # [l(7), r(1), 5, 3, 6, 4]
        if prices[r] < prices[l]:
            # [7, lr(1), 5, 3, 6, 4]
            l = r
        # 0 = max(0, 1 - 1)
        res = max(res, prices[r] - prices[l])

        # Second round through
        # [7, l(1), r(5), 3, 6, 4]
        # 4 = max(0, 5 - 1)

        # Fourth round through
        # [7, l(1), 5, 3, r(6), 4]
        # 5 = max(4, 6 - 1)
    return res
```