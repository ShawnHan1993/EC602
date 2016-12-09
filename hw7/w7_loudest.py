# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
from numpy import *
import scipy.io.wavfile as wavfile
def loudest_band(music,frame_rate,bandwidth):
    N=music.shape[0]
    music_f=fft.fft(music,N)
    BW=int(floor(bandwidth*1.0*N/(frame_rate*1.0)))
    low=0
    energy=0
    prev=0
    if len(music_f.shape)==1:
        for i in range(int(music_f.shape[0]/2)-BW+1):
            tmp=0
            if i==0:
                for k in range(BW):
                    tmp=tmp+abs(music_f[i+k])**2
            else:
                preItem=abs(music_f[i-1])**2
                netItem=abs(music_f[i+BW-1])**2
                tmp=prev-preItem+netItem
            if energy<tmp:
                low=i
                high=i+BW
                energy=tmp
            prev=tmp
    else:
        for i in range(int(music_f.shape[0]/2)-BW+1):
            tmp=0
            if i==0:
                for k in range(BW+1):
                    tmp=tmp+abs(music_f[i+k][0]+music_f[i+k][1])**2
            else:
                tmp=prev-abs(music_f[i-1][0]+music_f[i-1][1])**2+abs(music_f[i+BW][0]+music_f[i+BW][1])**2
            if energy<tmp:
                low=i
                high=i+BW
                energy=tmp
            prev=tmp

    filtered=[0]*N
    filtered[low:high]=music_f[low:high]
    filtered[(N-high):(N-low)]=music_f[(N-high):(N-low)]
    filtered=array(filtered)
    loudest=fft.ifft(filtered)
    loudest=loudest.real
    low=low*1.0*frame_rate/N
    high=low+bandwidth
    return low,high,loudest

if __name__=='__main__':
    frame_rate,music = wavfile.read("bach10sec.wav")
    low,high,loudest=loudest_band(music,frame_rate,100)
    cc=0