import os # to save recording to disk
from flask import request

def get_media(media_got):
    print("Media bucket script")
    print(media_got)
    audio_to_write=media_got.read()
    #write to server folder
    f = open('./Audios/test.wav', 'wb')
    #f.write(request.get_data("audio_data"))
    f.write(audio_to_write)
    f.close()

    return 1