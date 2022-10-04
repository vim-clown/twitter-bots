from twitter import TwitterHTTPError
import unicodedata
import requests
import time
import os
import requests
import os
import praw
import tweepy
from twitter import Twitter, OAuth
from pytwitter import Api


class Avth:
    def intra_avth():
        consumer_key = os.environ['consumer_key']
        consumer_secret = os.environ['consumer_secret']
        access_token_key = os.environ['access_token_key']
        access_token_secret = os.environ['access_token_secret']
        t = Twitter(auth=OAuth(access_token_key, access_token_secret,
                            consumer_key, consumer_secret))
        # auth2 = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
        # auth2.set_access_token(access_token_key, access_token_secret)
        # ap = tweepy.API(auth2, wait_on_rate_limit=True) 
    def greentext_avth():
        CONSUMERKEY = os.environ['CONSUMERKEY']
        CONSUMERSECRET = os.environ['CONSUMERSECRET']
        ACCESSTOKEN = os.environ['ACCESSTOKEN']
        ACCESSTOKENSECRET = os.environ['ACCESSTOKENSECRET']
        auth1 = tweepy.OAuth1UserHandler(CONSUMERKEY, CONSUMERSECRET)
        auth1.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)
        api1 = tweepy.API(auth1, wait_on_rate_limit=True)
        # Reddit Authentication
        reddit_read_only = praw.Reddit(
            user_agent= os.environ['user_agent'],
            client_id= os.environ['client_id'],
            client_secret= os.environ['client_secret'])
        # Target sub-reddit
        sub_reddit = reddit_read_only.subreddit("greentext") 
    def historymemes_avth():
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
        ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
        ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        spi = tweepy.API(auth, wait_on_rate_limit=True)
        # Reddit Authentication
        reddit_read_only = praw.Reddit(
            user_agent= os.environ['user_agent1'],
            client_id= os.environ['client_id1'],
            client_secret= os.environ['client_secret1'])
        # Target sub-reddit
        subreddit = reddit_read_only.subreddit("HistoryMemes")
        post_dict = {} 
    def apy2_avth():
        apy2 = Api(
        consumer_key= os.environ['CONSUMERKEY'],
        consumer_secret= os.environ['CONSUMERSECRET'],
        access_token= os.environ['ACCESSTOKEN'],
        access_secret= os.environ['ACCESSTOKENSECRET']
        ) 
    def apy_avth():
        apy = Api(
        consumer_key= os.environ['CONSUMER_KEY'],
        consumer_secret= os.environ['CONSUMER_SECRET'],
        access_token= os.environ['ACCESS_TOKEN'],
        access_secret= os.environ['ACCESS_TOKEN_SECRET']
        )  
    def creditbot_avth():
        c_CONSUMERKEY = os.environ['capi_key']
        c_CONSUMERSECRET = os.environ['capi_key_secret']
        c_ACCESSTOKEN = os.environ['caccess_token']
        c_ACCESSTOKENSECRET = os.environ['caccess_token_secret']
        c_auth1 = tweepy.OAuth1UserHandler(c_CONSUMERKEY, c_CONSUMERSECRET)
        c_auth1.set_access_token(c_ACCESSTOKEN, c_ACCESSTOKENSECRET)
        c_api1 = tweepy.API(c_auth1, wait_on_rate_limit=True)


class GreentextXHistorymemes:
    def poster(subr3dd1t, API_Param, ReplyCall, scr33n_name, covnt): 
        for post in subr3dd1t.new(limit=1):
            print(post.title, post.url)
            statuses = API_Param.user_timeline(count=covnt, include_rts=False, exclude_replies=True, screen_name=scr33n_name,tweet_mode='extended')
            if hasattr(post, "is_gallery"):
                print("Gallery post, sleeping.")
                time.sleep(300)
            else:
                tweet_list = []
                print(f"Fetched {len(statuses)} statuses for checking post duplicate")
                for status in statuses: 
                    '''removing links'''
                    splitted_status = status.full_text.lower().split(" https://")
                    parts = [phrase for phrase in splitted_status]
                    final_part = parts[0]
                    splitted_part = final_part.split("\n")
                    parts2 = [W for W in splitted_part]
                    final_part2 = parts2[0]
                
                    '''removing first element in the splitted tweet which may be >[word] , > or @''' 
                    processed_final_part2 = final_part2.split(" ")
                    final_part2_list = [word for word in processed_final_part2]
                    del final_part2_list[0]
                    final_part3 = " ".join(final_part2_list)
                    tweet_list.append(final_part3)
                print(tweet_list)
                
                '''removing first element in the splitted post title''' 
                processing_post = post.title.lower().split(" ")
                processed_post_list = [word for word in processing_post]
                del processed_post_list[0]
                processed_post_title = " ".join(processed_post_list)
                print(f"processed post tile: {processed_post_title}")
                
                if (processed_post_title in tweet_list):
                    print("False")
                    time.sleep(201) 
                else:
                    try:
                        print("True")
                        url = post.url
                        r = requests.get(url, allow_redirects=True)
                        print(r)
                        open('sample1.jpg', 'wb').write(r.content)
                        # response = b.shorten(post.permalink)
                        main_tweet = API.update_status_with_media(
                            status=post.title + "\n" + "#meme #history",
                            filename='sample1.jpg')
                        print("Posted")
                        os.remove('sample1.jpg')
                         
                        time.sleep(10)
                        try:
                            reply_tweet = ReplyCall.update_status(status="reddit.com" + post.permalink, 
                            in_reply_to_status_id=main_tweet.id, auto_populate_reply_metadata=True)
                            print("replied")
                        except Exception as shid:
                            print(shid)
                            print("couldn't reply")
                        ''' 
                        time.sleep(2)
                        try:
                            main.apy.hidden_reply(tweet_id=reply_tweet.id, hidden=True)
                            print("reply hidden successfuly")
                            
                        except Exception as repl:
                            print(repl)
                            print("couldn't hide reply")
                        '''
                        time.sleep(799)
                    except Exception as bruh_moment:
                        print(bruh_moment)
                        print("sleeping for 69 secs")
                        time.sleep(69) 
         
        
    def history_memes():
        GreentextXHistorymemes.poster('subreddit', 'spi', 'c_api1', 'ThomasPepeson', 20)

        
    def green_text():
        GreentextXHistorymemes.poster('sub_reddit', 'api1', 'c_api1', 'LeGreentext', 20) 


class Intra:
    def start():
        wordlist = ["NFTartist","Cryptoart","PolygonNFTs","CleanNFT",
            "nftcollectibles","#mfers","DrSoldmanGatchs","nftbuyer",
            "0xbotfather","NFTCommunity","cryptopunk",
            "opensea","cryptopunk","BAYC", "toomuchlag","NFTartwork",
            "yvgal","bored ape","NFT","PolygonNFTs",
            "nftart","nftcollectibles","#mfers","DrSoldmanGatchs",  
            "NFTcollection","0xbotfather","NFTMarketplace","Rarible",
            "nftcollectors","opensea","cryptopunk",
            "NFTsales","opensea"]

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
        except Exception as e:
            print(e)
            time.sleep(500)
            
