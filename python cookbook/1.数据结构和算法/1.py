def phone_number_out (record):
    first, second, *last = record
    print(*last)
records = ('Dave', '@email.com', '13814536225', '18844470055')
phone_number_out (records)
########
import heapq
portfolio = [
    {'name':'IBM', 'shares':100, 'price':91.1},
    {'name':'AAPL', 'shares':50, 'price':543.22},
    {'name':'FB', 'shares':200, 'price':21.09},
    {'name':'HPQ', 'shares':35, 'price':31.75},
    {'name':'YHOO', 'share':45, 'price':16.35},
    {'name':'ACME', 'share':75, 'price':115.65}
]
cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
cheap
expensive

nums = (1,8,2,23,7,-4,18,23,42,37,2)
nums_list = list(nums)  #转换为列表，因为heapq.heapify只接受列表
heapq.heapify(nums_list) #将列表转换为堆，堆有特性：堆[0]总是最小的那个
heapq.heappop(nums_list) #弹出堆的第一个元素
heapq.heappop(nums_list) #连续弹出