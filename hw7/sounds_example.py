# Support for sound is provided 
# in a number of modules. Some
# are part of the standard library,
# but others are not. Everything we 
# use is part of the Anaconda distribution
# of python.
# WAV file support
import scipy.io.wavfile as wavfile

# sound playing
import PyQt4.QtGui as qt

# sleep while sound is playing
import time

# arrays
import numpy

# plotting facilities
import matplotlib.pyplot as pyplot

def read_wave(fname,debug=False):
    "return information about and time signal in the WAV file fname"
    frame_rate,music = wavfile.read(fname)
    print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels

def wavplay(fname):
    "play a sound, and sleep until it is finished"
    qt.QSound.play(fname)
    music,frame_rate,nframes,nchannels = read_wave(fname)
    time.sleep(nframes/frame_rate)


fname = "bach10sec.wav"

# Plot the sound
music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
if nchannels > 1:
    music = music.sum(axis=1)


# Listen to the sound
wavplay('bach10sec.wav')
wavplay('scary.wav')