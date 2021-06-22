# https://leetcode-cn.com/problemset/algorithms/?topicSlugs=array&listId=ex0k24j

'''
买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''

# class Solution:
#     def maxProfit(self, prices):
#         min_price = prices[0]
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             max_profit = max(max_profit, prices[i] - min_price)
#         return max_profit
#
# s = Solution()
# ret = s.maxProfit([7,1,5,3,6,4])
# print(ret)


'''
买卖股票的最佳时机2

给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

# def maxProfit(arr):
#     sum = 0
#     for i in range(1, len(arr)):
#         if arr[i-1] < arr[i]:
#            sum += arr[i] - arr[i-1]
#     return sum
#
# arr = [7,1,5,3,6,4]
# ret = maxProfit(arr)
# print(ret)


'''
多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

https://leetcode-cn.com/problems/majority-element/
'''
# class Solution:
#     def majorityElement(self, nums):
#         count = 0
#         flag = 0
#         for i in range(len(nums)):
#             if count == 0:
#                 flag = nums[i]
#             if flag == nums[i]:
#                 count += 1
#             else:
#                 count -= 1
#         return flag
#
# s = Solution()
# ret = s.majorityElement([2,2,1,1,1,2,2])
# print(ret)

'''
存在重复元素

给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

https://leetcode-cn.com/problems/contains-duplicate/
'''
# class Solution:
#     def containsDuplicate(self, nums):
#         if len(set(nums)) != len(nums):
#             return True
#         else: return False