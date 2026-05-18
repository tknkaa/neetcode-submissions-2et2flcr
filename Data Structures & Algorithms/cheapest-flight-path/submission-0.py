class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            tmp = prices.copy()
            for flight in flights:
                start = flight[0]
                goal = flight[1]
                weight = flight[2]
                if prices[start] + weight < tmp[goal]:
                    tmp[goal] = prices[start] + weight
            prices = tmp
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]