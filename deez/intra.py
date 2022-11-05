import deez
import time

    
def start(XAuth):
    wordlist = ["NFTartist","Cryptoart","PolygonNFTs","CleanNFT","nftcollectibles","#mfers","DrSoldmanGatchs","nftbuyer",
                "0xbotfather","NFTCommunity","cryptopunk","opensea","cryptopunk","BAYC", "toomuchlag","NFTartwork",
                "yvgal","bored ape","NFT","PolygonNFTs","nftart","nftcollectibles","#mfers","DrSoldmanGatchs",  
                "NFTcollection","0xbotfather","NFTMarketplace","Rarible","nftcollectors","opensea","cryptopunk","NFTsales","opensea"] 
    def search_tweets(q, count=1):
        return XAuth.search.tweets(q=q + " -giveaway -LIKEFOLLOWANDRETWEET! -#NFTGiveaway -towin -away -retweet -airdrop -drop -RT",
            result_type='recent', count=count)
    def retweet_tweet(tweet):
        try:
            result = XAuth.statuses.retweet._id(_id=tweet['id'])
            print("Retweeted: %s" % (result['text']))
            return result
        except deez.TwitterHTTPError as e:
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
        time.sleep(200)
    try:
        for word in wordlist:
            auto_retweet(word, 1) 
        deez.history_memes()
    except Exception as e:
        print(e)
        time.sleep(500)
        deez.history_memes()