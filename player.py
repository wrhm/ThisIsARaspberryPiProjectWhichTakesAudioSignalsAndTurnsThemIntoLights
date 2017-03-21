# https://www.daniweb.com/programming/software-development/threads/491663/how-to-open-and-play-mp3-file-in-python
'''
TODOs
	- https://www.pygame.org/docs/ref/mixer.html
	- https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_volume
	- http://stackoverflow.com/questions/30571955/get-playing-wav-audio-level-as-output
		- use rms to get loud intervals
		- do this in preprocessing, then use music.get_pos to see if near a
		  loud interval. if so, spit out high voltage to lights
'''

''' pg_playmp3f.py
play MP3 music files using Python module pygame
pygame is free from: http://www.pygame.org
(does not create a GUI frame in this case)
'''
import pygame as pg
def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    f = open('%s.txt'%(music_file.split('/')[-1].split('.')[0]),'wb')
    soundObj = pg.mixer.Sound(music_file)
    f.write(pg.mixer.Sound.get_raw(soundObj))
    f.close()
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)
# music_file = "meseeks.mp3"
music_file = "Machu_Picchu_-_The_Strokes_OFFICIAL_ALBUM_VERSION_.wav"
# optional volume 0 to 1.0
volume = 0.8
play_music('../AudioFiles/%s'%music_file, volume)