# 121. Best Time to Buy and Sell Stock

def maxProfit1(prices):
        buy,buy_i,sell,sell_i=100000000000,0,0,0
        for i in range(len(prices)-1):
            print(prices[i],prices[i+1])
            if prices[i] < prices[i+1]:
                
                if buy > prices[i]:
                    buy = prices[i]
                    buy_i=i
                if sell < prices[i+1]:
                    sell=prices[i+1]
                    sell_i=i+1
            else:
                if prices[i]==7:
                    print(prices[i+1], buy < prices[i+1]," boop")
                if buy > prices[i+1]:
                    buy = prices[i+1]
                    buy_i=i+1
            print(buy,sell)
            print(buy_i,sell_i)
            print("===") 
        if buy_i < sell_i and  sell - buy > 0:
            return sell - buy
        else:
            return 0

# upper try failed 


def maxProfit(prices):
        maxProfit = 0
        l,r=0,1
        #find the max diff while ensuring l < r. 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxProfit = max(profit,maxProfit)
            else:
                l=r  # r is less than l, so move r forward.
            r+=1 
        return maxProfit

prices=[2,4,1]
print(maxProfit(prices))
