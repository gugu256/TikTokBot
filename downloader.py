import requests

def download(memes):
    for url in memes:
        name = url.replace("https://i.redd.it/", "")
        with open("memes/"+name, "wb") as f:
            f.write(requests.get(url).content)