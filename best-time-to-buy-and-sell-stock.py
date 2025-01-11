def maxProfit(self, prices: list[int]) -> int:
        _N = len(prices)

        buy = 0
        sell = 1
        profit = 0
        while buy <= _N-2:
            
            if sell < _N:
                calc = prices[sell] - prices[buy]
                profit = max(profit, calc)
                sell += 1
            
            else:
                buy += 1
                sell = buy+1
        
        return profit
