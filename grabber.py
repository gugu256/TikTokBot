import requests
import random

def get_post():
    r = requests.get("https://reddit.com/r/amitheasshole.json", headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.98'})
    p = r.json()
    p = p["data"]["children"]
    posts = []

    for post in p:
        if post["data"]["title"].startswith("AITA"):
            posts.append(post["data"])
        else:
            pass

    i = random.randint(0, len(posts))

    return {"content": posts[i]["selftext"].replace("AITA", "Am I The Ah Hole"), "title": posts[i]["title"].replace("AITA", "Am I The Ah Hole")}