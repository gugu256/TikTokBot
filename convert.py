from PIL import Image
import os
import moviepy.editor as mp



def convert_all():
    files = os.listdir("memes")
    for file in files:
        if ".jpg" in file or ".png" in file:
            img = Image.open("memes/" + file)
            img.save("memes/" + file[0:-4] + ".gif")
            
            clip = mp.VideoFileClip("memes/" + file[0:-4] + ".gif")
            clip.write_videofile("memes/" + file[0:-4] + ".mp4")
            os.remove("memes/" + file)
            os.remove("memes/" + file[0:-4] + ".gif")