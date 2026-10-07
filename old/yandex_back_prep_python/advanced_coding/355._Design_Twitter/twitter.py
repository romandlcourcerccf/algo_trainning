from typing import List


class Twitter:
    def __init__(self):
        self._users_tweests = {}
        self._followed = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self._users_tweests:
            self._users_tweests[userId] = []

        self._users_tweests[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        if userId in self._followed:
            user_followed = self._followed[userId]
        else:
            user_followed = set()

        user_followed = user_followed.copy()
        user_followed.add(userId)

        for id in user_followed:
            tweets += self._users_tweests[id]

        tweets.sort()
        tweets = tweets[:10]

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self._followed:
            self._followed[followerId] = set()

        self._followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._followed[followerId].remove(followeeId)
