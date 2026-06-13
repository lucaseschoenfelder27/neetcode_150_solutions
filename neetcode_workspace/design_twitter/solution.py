import heapq

class Twitter(object):

    def __init__(self):
        '''
            users = {
                "<userId>" : {
                    followers : []
                    tweets : []
                }
            }
            tweets_maxhp = [
                (tweetId, userId)
            ]
        '''
        self.users = {}
        self.tweets_maxhp = []
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.users:
            self.users.setdefault(userId, {"followers": [], "tweets" : []})
        self.users[userId]["tweets"].append(tweetId)
        heapq.heappush(self.tweets_maxhp, (-tweetId, userId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        newsFeed = []
        for tweetId, tweetAuthorId in self.tweets_maxhp:
            if tweetAuthorId == userId or tweetAuthorId in self.users[userId]["followers"]:
                newsFeed.append(-tweetId)
        return newsFeed

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.users[followerId]["followers"]:
            self.users[followerId]["followers"].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.users[followerId]["followers"]:
            self.users[followerId]["followers"].remove(followeeId)