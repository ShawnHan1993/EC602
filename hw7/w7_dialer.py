# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
from numpy import *
import scipy.io.wavfile as wavfile

def dialer(file_name,frame_rate,phone,tone_time):
    lowF={1:697,2:697,3:697,4:770,5:770,6:770,7:852,8:852,9:852,0:941}
    higF={1:1209,2:1336,3:1477,4:1209,5:1336,6:1477,7:1209,8:1336,9:1477,0:1336}
    outputWav=array([])
    for i in range(len(phone)):
        curNum=int(phone[i])
        LF=lowF[curNum]
        HF=higF[curNum]
        t=linspace(0,tone_time,int(frame_rate*tone_time))
        tmp=cos(2*pi*LF*t)+cos(2*pi*HF*t)
        outputWav=concatenate([outputWav,tmp])
    wavfile.write(file_name,frame_rate,outputWav)
    print(outputWav)
if __name__=='__main__':
    dialer('test.wav',8000,'123',0.5)