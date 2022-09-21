def start():
    # the deferred imports fix a circular import issue 
    import time
    from historymemes import history_memes
    from main import t, wordlist
    from twitter import TwitterHTTPError
    def search_tweets(q, count=1):
        return t.search.tweets(q=q + " -giveaway -LIKEFOLLOWANDRETWEET! -#NFTGiveaway -towin -away -retweet -airdrop -drop -RT",
            result_type='recent', count=count)

    def retweet_tweet(tweet):
        try:
            result = t.statuses.retweet._id(_id=tweet['id'])
            print("Retweeted: %s" % (result['text']))
            return result
        except TwitterHTTPError as e:
            print("Error: ", e)
            return None

    def auto_retweet(q, count):
        result = search_tweets(q, count)
        a = result['statuses'][0]['user']['screen_name']
        print(a)
        success = 0
        for tweet in result['statuses']:
            if retweet_tweet(tweet) is not None:
                success += 1
        print("We retweeted a total of %i out of %i tweets" % (success, len(result['statuses'])))
        time.sleep(100)

    try:
        for word in wordlist:
            auto_retweet(word, 1)
        
        history_memes()

    except Exception as e:
        print(e)
        time.sleep(500)
        history_memes()
