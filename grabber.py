import requests
import random



r = requests.get("https://reddit.com/r/memes.json", headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.98'})
p = r.json()
p = p["data"]["children"]

def get_memes(max=25):
    memes = []

    for meme in p:
        if meme["data"]["url_overridden_by_dest"] != "":
            memes.append(meme["data"]["url_overridden_by_dest"])
        else:
            pass

    i = random.randint(0, len(memes))
    print(len(memes))
    return memes[0:max]