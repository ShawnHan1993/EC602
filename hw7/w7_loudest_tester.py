import unittest
from numpy import pi,cos,sin,linspace,ones_like,zeros_like
#import matplotlib.pyplot as pyplot
import scipy.io.wavfile as wavfile
from w7_loudest import loudest_band
import time

def read_wave(fname,debug=False):
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels

music,frame_rate,nframes,nchannels = read_wave("bach10sec.wav")
if nchannels > 1:
    music = music.sum(axis=1)

def match(w,ref):
    "return the relative similarity of w and ref"
    energy = (abs(ref)**2).sum()
    error = (abs(w-ref)**2).sum() 
    return error/energy

class loudestTestCase(unittest.TestCase):
    def test_find_band(self):
        frame_rate,T,ftest,bandwidth = 1000,1,100,10
        m = sin(2*pi*ftest * linspace(0,T,T*frame_rate))
        low,high,filtered = loudest_band(m,frame_rate,bandwidth)
        self.assertEqual(m.shape,filtered.shape)
        self.assertLess(low,ftest,msg="low of band incorrect")
        self.assertLess(ftest,high,msg="high of band incorrect")
        self.assertEqual(bandwidth,high-low,msg="high-low must match bandwidth")
        error=match(filtered,m)
        self.assertLess(error,0.1,msg="filtered signal incorrect")

    def test_find_energy(self):
        frame_rate,T,ftest,bandwidth = 10000,1,100,10
        t = linspace(0,T,T*frame_rate)
        m = zeros_like(t)
        for a,f in [(1,10),(1,11),(1,12),(2,30)]:
            m += a*cos(2*pi*f*t)
        low,high,filtered = loudest_band(m,frame_rate,bandwidth)
        self.assertEqual(m.shape,filtered.shape)
        self.assertLessEqual(low,30,msg="low of band incorrect")
        self.assertLessEqual(30,high,msg="high of band incorrect")
        self.assertEqual(bandwidth,high-low)

    def test_find_band_split(self):
        frame_rate,T,ftest,bandwidth = 10000,1,100,10
        t = linspace(0,T,T*frame_rate)
        m = sin(2*pi*ftest*t)+sin(2*pi*(ftest+0.8*bandwidth)*t)
        low,high,filtered = loudest_band(m,frame_rate,bandwidth)
        self.assertEqual(m.shape,filtered.shape)
        self.assertLessEqual(low,ftest,msg="low of band incorrect")
        self.assertLessEqual(ftest+.8*bandwidth,high,msg="high of band incorrect")
        self.assertEqual(bandwidth,high-low)
        error=match(filtered,m)
        self.assertLess(error,0.1,msg="filtered signal incorrect")

    def test_find_band_dc(self):
        frame_rate,T,ftest,bandwidth = 1000,1,100,20
        t = linspace(0,T,T*frame_rate)
        m = ones_like(t) + sin(2*pi*bandwidth//2)
        low,high,filtered = loudest_band(m,frame_rate,bandwidth)
        self.assertEqual(m.shape,filtered.shape)
        self.assertEqual(high,bandwidth)
        self.assertEqual(low,0)
        self.assertLess(match(filtered,m),0.1,msg="filtered signal incorrect")


class loudest_efficiency_TestCase(unittest.TestCase):
    def test_bach(self):
        start = time.time()
        low,high,filtered = loudest_band(music,frame_rate,75)
        duration = time.time() - start
        if duration > 1.0:
                print("WARNING: my analysis of bach10sec takes 0.3 s, yours took {:.3f} s".format(duration))
                print('the actual checker will fail you on this test. Passing this is extra credit.')
        self.assertEqual(music.shape,filtered.shape)        
        self.assertAlmostEqual(low/823.5,1.0,2)
        self.assertAlmostEqual(high/898.3,1.0,2)
    
if __name__ == '__main__':
    unittest.main()