# TODO :
#      Assemble video
#      Publish video

import grabber
import downloader
import convert

downloader.download(grabber.get_memes(3))
convert.convert_all()