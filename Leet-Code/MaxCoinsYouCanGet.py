class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)

        n = len(piles) // 3
        i = 0
        count = 0

        while n > 0:
            if i % 2 == 1:
                count += piles[i]
                n     -= 1
            i += 1
        return count
