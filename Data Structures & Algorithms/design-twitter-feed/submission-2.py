from sortedcontainers import SortedList, SortedSet
from operator import neg
time = 0
class Tweet:
    def __init__(self, tweetId):
        global time
        self.tweetId = tweetId
        self.time = time
        time += 1
    
    def __gt__(self, tweet):
        return self.time < tweet.time
    
    def __lt__(self, tweet):
        return self.time > tweet.time


class User:
    def __init__(self):
        self.tweets = []
        self.followList = SortedSet()

class Twitter:

    def __init__(self):
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User()
        user = self.users[userId]
        user.tweets.append(Tweet(tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        user = self.users[userId]
        tweetsList = []
        tweetsList += user.tweets
        for follow in user.followList:
            tweetsList += self.users[follow].tweets
        tweetsList = list(set(tweetsList))
        heapq.heapify(tweetsList)
        return [x.tweetId for x in heapq.nsmallest(10, tweetsList)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User()
        user = self.users[followerId]
        user.followList.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User()
        user = self.users[followerId]
        user.followList.discard(followeeId)
