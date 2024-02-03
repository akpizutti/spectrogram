import sys
from scipy.io import wavfile
import scipy.misc
from numpy import *
from numpy.fft import *
from matplotlib.pyplot import *
from PIL import Image

MAGIC_NUMBER = 1 / 18.8 * 255
sample_rate = 44100



if(len(sys.argv) < 2 ):
    print("Numero de argumentos invalido.")
else:
    filename = sys.argv[1]
    img = Image.open(filename)
    spectrogram = flip(asarray(img).transpose(), 1)
    block_size = spectrogram.shape[1] * 2
    blocks = spectrogram.shape[0]
    out_length = block_size * blocks

    print(spectrogram.shape)
    print("Block size: " + str(block_size))
    print("Blocks to be processed: " + str(blocks))
    print("Resulting file length: " + str(out_length) + " samples")

    samples = empty(out_length, dtype=complex128)
    
    phase_matrix = zeros((blocks,int(block_size/2)), dtype=float)
    for i in range(phase_matrix.shape[0]):
        for j in range(phase_matrix.shape[1]):
            phase_matrix[i][j] = (i * j * 2 * pi)

            # phase increment from https://github.com/android/codelab-android-wavemaker/blob/master/app/src/main/cpp/Oscillator.cpp
            # phaseIncrement_ = (TWO_PI * FREQUENCY) / (double) sampleRate;
            

    for i in range(blocks):
    
        amplitudes = exp(spectrogram[i] / MAGIC_NUMBER)
        amplitudes[0] = 0.0 # remove DC
        phases = phase_matrix[i]


        # transformar isso em um vetor de numeros complexos
        spectrum = empty(block_size, dtype=complex128)

        real = amplitudes * cos(phases)
        imag = amplitudes * sin(phases)

        spectrum.real = concatenate((real,flip(real)))
        spectrum.imag = concatenate((imag,flip(imag)))


        block = ifft(spectrum)

        samples[i*block_size:(i+1)*block_size] = block

    output = zeros(out_length, dtype=int16)
    max = max(samples.real)
    output = int16(samples.real / max * 32767)

    plot(output)
    show()


    wavfile.write('output.wav', 44100, output)
    
    





    
        
        
