# TODO:
# function to convert dB values to linear
# adjust gain of output signal
# mono summing that doesn't take forever
# support other file types



import sys
from scipy.io import wavfile
import scipy.misc
from numpy import *
from numpy.fft import *
from matplotlib.pyplot import *
from PIL import Image



if(len(sys.argv) < 2 ):
    print("Numero de argumentos invalido.")
else:
    filename = sys.argv[1]
    block_size = 8192 

    samplerate,data = wavfile.read(filename)
    file_length, channels = data.shape
    nyquist = samplerate/2
    blocks = int(floor(file_length / block_size))

    # print(data)

    print("Samplerate: " + str(samplerate))
    print("Length: " + str(file_length) + " samples")
    print("Block size: " + str(block_size))
    print("Number of blocks to process: " + str(blocks))

    mono = zeros(file_length, dtype=int)

    # TODO: find better solution to this, takes too long (python why)
    # sum all channels to mono
    # if(channels > 1 ):
    #     for i in range(file_length):
    #         for j in range(channels):
    #             #print(data[i][j])
    #             mono[i] = (mono[i] + data[i][j])
    #         mono[i] = int(mono[i]/channels)


    # using only left channel for now, summing to mono takes too long
    data_t = data.transpose()
    mono = data_t[0]



    # print(mono)


    
    spectrogram = empty((blocks, int(block_size/2)))
    for i in range(blocks):
        # print("Processing block " + str(i))

        #calculate FFT of a single block
        spectrum = fft(mono[i*block_size::], n=block_size)

        amplitudes = abs(spectrum[0:int(block_size/2)])
        # frequency = n * Fs / N, where n is the index in the array, Fs is the sample rate and N is the size of the FFT.


        spectrogram[i] = amplitudes

    print(spectrogram.shape)
    




    spectrogram = spectrogram.transpose()









    if(len(spectrogram) > 0):
        
        figure(figsize=array([210,297]) / 25.4)

        t = linspace(0, 3, spectrogram.shape[1]+1)
        f = linspace(0, 10000, spectrogram.shape[0]+1)
        
        yscale("symlog") # this only works for the matplotlib plot, not for the saved image

        # imshow(log(spectrogram), interpolation='none')
        # pcolormesh(t, f, log(spectrogram), antialiased=False)
        

        max = amax(log(spectrogram))


        out_array = (log(spectrogram) / max * 255).astype(uint8)
        # print(out_array)

        # imshow(out_array)
        # show()

        img = Image.fromarray(out_array, "L")
        img.save(filename + "_spectrogram.png")


