from twitter import Twitter


def test_twitter():
    twitter = Twitter()

    twitter.postTweet(userId=1, tweetId=5)
    twitter.postTweet(userId=1, tweetId=6)

    twitter.postTweet(userId=2, tweetId=7)
    twitter.postTweet(userId=2, tweetId=8)

    feed = twitter.getNewsFeed(userId=1)

    assert len(feed) == 2

    assert 5 in feed
    assert 7 not in feed

    twitter.follow(1, 2)

    feed = twitter.getNewsFeed(userId=1)

    assert 5 in feed
    assert 7 in feed

    twitter.unfollow(1, 2)

    feed = twitter.getNewsFeed(userId=1)

    assert 5 in feed
    assert 7 not in feed
