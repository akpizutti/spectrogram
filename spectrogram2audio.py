import sys
from scipy.io import wavfile
import scipy.misc
from numpy import *
from numpy.fft import *
from matplotlib.pyplot import *
from PIL import Image

MAGIC_NUMBER = 1 / 18.8 * 255



if(len(sys.argv) < 2 ):
    print("Numero de argumentos invalido.")
else:
    filename = sys.argv[1]
    img = Image.open(filename)
    spectrogram = asarray(img).transpose()
    block_size = spectrogram.shape[1] * 2
    blocks = spectrogram.shape[0]
    out_length = block_size * blocks

    print(spectrogram.shape)
    print("Block size: " + str(block_size))
    print("Blocks to be processed: " + str(blocks))
    print("Resulting file length: " + str(out_length) + " samples")

    samples = empty(out_length, dtype=complex128)

    for i in range(blocks):
    
        amplitudes = exp(spectrogram[i] / MAGIC_NUMBER)
        amplitudes[0] = 0.0 # remove DC
        amplitudes_conj = concatenate((amplitudes , flip(amplitudes))) / 2

        # transformar isso em um vetor de numeros complexos
        spectrum = empty(len(amplitudes_conj), dtype=complex128)
        spectrum.real = amplitudes_conj
        spectrum.imag = zeros(len(amplitudes_conj))

        block = ifft(spectrum)
        #print(block.imag)

        samples[i*block_size:(i+1)*block_size] = block

    output = zeros(out_length, dtype=int16)
    max = max(samples.real)
    output = int16(samples.real / max * 32767)
    wavfile.write('output.wav', 44100, output)
    
    





    
        
        
