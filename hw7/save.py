        for k in range(int(round(frame_rate*tone_time))):
            LF=lowF[curNum]
            HF=higF[curNum]
            curPoint=(cos(k*LF*2*pi/frame_rate)+cos(k*HF*2*pi/frame_rate))
            outputWav.append(curPoint)