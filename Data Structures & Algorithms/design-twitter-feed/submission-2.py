import heapq

class Twitter:

    def __init__(self):
        self.followMap: Dict[int, List[int]] = {}
        self.tweetMap: Dict[int, List[tuple[int, int]]] = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ten_tweets = []
        userIds = list(set([userId] + self.followMap.get(userId, [])))
        heap = []
        for id in userIds:
            if id in self.tweetMap:
                index = len(self.tweetMap[id]) - 1
                count = self.tweetMap[id][index][0]
                heap.append((-count, id, index))
        heapq.heapify(heap)
        for _ in range(10):
            if len(heap) == 0:
                return ten_tweets
            newest = heapq.heappop(heap)
            userId = newest[1]
            index = newest[2]
            ten_tweets.append(self.tweetMap[userId][index][1])
            if index - 1 >= 0:
                heapq.heappush(heap, (-self.tweetMap[userId][index - 1][0], userId, index - 1))
        return ten_tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = []

        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = []
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
