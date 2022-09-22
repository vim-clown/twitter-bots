def history_memes():
    from greentext import green_text
    import main
    import time
    import os
    import requests
    from main import subreddit
    for post in subreddit.hot(limit=5):
        print(post.title, post.url)
        statuses = main.spi.user_timeline(count=20, include_rts=False, exclude_replies=True)
        if hasattr(post, "is_gallery"):
            print("Gallery post, sleeping.")
            time.sleep(300)
        else:
            print(f"Fetched {len(statuses)} statuses for checking post duplicate")
            status_list = []
            for status in statuses:
                status_list.append(status.text.lower())
            processed_title = post.title.lower() + "\n" + "#meme #history"
            if processed_title in status_list:
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
                    this = main.spi.update_status_with_media(
                        status=post.title + "\n" + "#meme #history",
                        filename='sample1.jpg')
                    print("Posted")
                    os.remove('sample1.jpg')
                         
                    time.sleep(10)
                    try:
                        that = main.c_api1.update_status(status="reddit.com" + post.permalink, 
                        in_reply_to_status_id=this.id, auto_populate_reply_metadata=True)
                        print("replied")
                    except Exception as shid:
                        print(shid)
                        print("couldn't reply")

                    ''' 
                    time.sleep(2)
                    try:
                        main.apy.hidden_reply(tweet_id=that.id, hidden=True)
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
                    history_memes()
                        
                        
    green_text()                   
    