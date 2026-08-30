class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        ans = 0
        for i in range(min(len(prices), len(discounts))):
            ans += prices[i] * (100 - discounts[i]) / 100

        ans += sum(prices[len(discounts):])

        return ans
        