from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        last_bought = 0
        total_earned = 0
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1] and last_bought == 0:
                # going up
                last_bought = prices[i]
                #print("bought at", prices[i])
                if prices[i]==0:
                    last_bought = .0001 #hotfix for price = 0 because this scenario is stupid
            if prices[i] > prices[i+1]:  
                # going down
                if last_bought != 0:
                    #print("sold at", prices[i])
                    total_earned += prices[i] - int(last_bought)
                    last_bought = 0
        #if you're still holding at the end
        if last_bought != 0:
            #print("sold at", prices[-1])
            total_earned += prices[-1] - int(last_bought)
            last_bought = 0   
        
        return total_earned 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)