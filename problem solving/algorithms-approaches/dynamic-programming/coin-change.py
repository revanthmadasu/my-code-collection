class Solution:
    def coinChange(self, coins, amount):
        num_of_coins = len(coins)
        dp_memory = [0]
        for i in range(amount):
            dp_memory.append(amount+1)
        for cur_amount in range(1,amount+1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    dp_memory[cur_amount] = min(dp_memory[cur_amount-coin]+1, dp_memory[cur_amount])
        return -1 if dp_memory[amount] > amount else dp_memory[amount]

print(Solution().coinChange([1,2,5],3))