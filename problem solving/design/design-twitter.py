'''
    Problem: https://leetcode.com/problems/design-twitter/
    Concepts: Design, LinkedList
    performance: 69.98% runtime, 27.73% memory
'''
'''
tweets linkedlist:
node: {
    userId,
    tweetId,
    next*
}
'''
from typing import List
class Twitter:
    def __init__(self):
        # key is userid, value is a set of follower user ids
        self.followersMap = dict()
        self.followingMap = dict()
        self.newsFeedMap = dict()
        # key - userid, val - list
        self.tweetsMap = dict()
        self.currentTime = 0
        # key: tweetid, val: time
        self.tweetsTimeline = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsMap:
            self.tweetsMap[userId] = []
        self.tweetsMap[userId].append(tweetId)
        self.tweetsTimeline[tweetId] = self.currentTime
        self.currentTime += 1
        tweetNode = dict()
        tweetNode['userId'] = userId
        tweetNode['tweetId'] = tweetId
        tweetNode['next'] = self.newsFeedMap[userId] if userId in self.newsFeedMap else None
        self.newsFeedMap[userId] = tweetNode
        if (userId in self.followersMap):
            followers = self.followersMap[userId]
            for followerId in followers:
                tweetNode = dict()
                tweetNode['userId'] = userId
                tweetNode['tweetId'] = tweetId
                tweetNode['next'] = self.newsFeedMap[followerId] if followerId in self.newsFeedMap else None
                self.newsFeedMap[followerId] = tweetNode


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.newsFeedMap:
            return []
        count = 0
        res = []
        newFeedList = self.newsFeedMap[userId]
        curNode = newFeedList
        while count < 10 and curNode:
            res.append(curNode['tweetId'])
            count += 1
            curNode = curNode['next']
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followersMap:
            self.followersMap[followeeId] = set()
        if followerId not in self.followingMap:
            self.followingMap[followerId] = set()
        if followerId in self.followersMap[followeeId]:
            return
        self.followersMap[followeeId].add(followerId)
        self.followingMap[followerId].add(followeeId)
        # after following, change news feed of the follower
        if followerId not in self.newsFeedMap:
            self.newsFeedMap[followerId] = None
        newsFeed = self.newsFeedMap[followerId]
        curNode = newsFeed
        prevNode = None
        if followeeId not in self.tweetsMap:
            self.tweetsMap[followeeId] = []
        tweets = self.tweetsMap[followeeId]
        for i in range(len(tweets)-1, -1, -1):
            tweetTime = self.tweetsTimeline[tweets[i]]
            while curNode and self.tweetsTimeline[curNode['tweetId']] > tweetTime:
                prevNode = curNode
                curNode = curNode['next']
            newTweetNode = dict()
            newTweetNode['userId'] = followeeId
            newTweetNode['tweetId'] = tweets[i]
            newTweetNode['next'] = curNode
            if prevNode:
                prevNode['next'] = newTweetNode
            else:
                self.newsFeedMap[followerId] = newTweetNode
            curNode = newTweetNode


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.followingMap) or (followeeId not in self.followersMap):
            # print(f'self.followingMap')
            return
        self.followingMap[followerId].remove(followeeId)
        self.followersMap[followeeId].remove(followerId)
        # remove items from newsfeed
        newsFeed = self.newsFeedMap[followerId]
        curNode = newsFeed
        prevNode = None
        while curNode:
            if curNode['userId'] == followeeId:
                if prevNode:
                    prevNode['next'] = curNode['next']
                else:
                    self.newsFeedMap[followerId] = curNode['next']
            else:
                prevNode = curNode
            curNode = curNode['next']


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)