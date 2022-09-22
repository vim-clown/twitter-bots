def green_text():
    from intra import start
    import main
    import time
    import os
    import requests
    from main import sub_reddit
    for post in sub_reddit.hot(limit=5):
        print(post.title, post.url)
        statuses = main.api1.user_timeline(count=40, include_rts=False, exclude_replies=True, screen_name='LeGreentext',tweet_mode='extended')
        if hasattr(post, "is_gallery"):
            print("Gallery post, sleeping.")
            time.sleep(300)
        else:
            print(f"Fetched {len(statuses)} statuses for checking post duplicate")
            status_list = []
            for status in statuses:
                splitted_status = status.full_text.lower().split(" https://")
                parts = [phrase for phrase in splitted_status]
                final_part = parts[0] 
                status_list.append(final_part)
            print(status_list)
            if (post.title.lower() in status_list):
                print("False")
                time.sleep(200)
            else:
                try:
                    print("True")
                    url = post.url
                    r = requests.get(url, allow_redirects=True)
                    print(r)
                    open('sample2.jpg', 'wb').write(r.content)
                    # response = b.shorten(post.permalink)
                    this2 =  main.api1.update_status_with_media(
                        status=post.title, filename='sample2.jpg')
                    print("Posted")
                    os.remove('sample2.jpg')

                    time.sleep(10)
                    try:
                        that2 = main.c_api1.update_status(status="reddit.com" + post.permalink, 
                        in_reply_to_status_id=this2.id, auto_populate_reply_metadata=True)
                        print("replied")
                    except Exception as shid:
                        print(shid)
                        print("couldn't reply")

                    '''
                    time.sleep(2)
                    try:
                        main.apy2.hidden_reply(tweet_id=that2.id, hidden=True)
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
                    green_text()
    
    start()