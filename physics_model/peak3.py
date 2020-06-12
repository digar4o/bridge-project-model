from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import peakutils
import sys



#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a(x):

    def smooth(x,window_len=11,window='hanning'):

        if window_len<3:
            return x

        
        if x.ndim != 1:
            raise ValueError('smooth only accepts 1 dimension arrays.')

        if x.size < window_len:
            raise ValueError('Input vector needs to be bigger than window size.')



        s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
        #print(len(s))
        if window == 'flat': #moving average
            w=np.ones(window_len,'d')
        else:
            w=eval('np.'+window+'(window_len)')

        y=np.convolve(w/w.sum(),s,mode='valid')
        return y


    fs_rate, signal = wavfile.read(x)


    print ("Frequency sampling", fs_rate)
    l_audio = len(signal.shape)
    print ("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    N = signal.shape[0]
    print ("Complete Samplings N", N)
    secs = N / float(fs_rate)
    print ("secs", secs)
    Ts = 1.0/fs_rate # sampling interval in time
    print ("Timestep between samples Ts", Ts)
    t = scipy.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(N//2)] # one side FFT range
    freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N//2)] # one side frequency range
    fft_freqs_side = np.array(freqs_side)


    smoothed=smooth(abs(FFT_side),225,'hanning')
    #smoothedX=smooth(freqs_side, 45, 'hanning')
    X = np.linspace(0, fs_rate/2, smoothed.shape[0] , endpoint=True)
    indexes = peakutils.indexes(smoothed, thres=0.1/max(smoothed), min_dist=20)

    #yplt.plot(freqs_side, abs(FFT_side))
    #plt.plot(X, smoothed)
    #plt.plot(X[indexes],smoothed[indexes], marker="o", ls="", ms=3 )

    #plt.xlabel('Frequency (Hz)')
    #plt.ylabel('Count single-sided')
    #plt.show()

#put in bounds for peak to be found below, will add functionality for multiple peaks later

 	       
    for i in indexes:
        if X[i] > 1800:  		
            if X[i] < 2000:  
                return X[i]




