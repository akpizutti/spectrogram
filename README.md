# What it is
Two python scripts: one to generate a spectrogram from an audio file, and another to generate an audio file from an image interpreted as a spectrogram.

# Spectrogram generation
Usage:
```
python spectrogram.py <input_wav_file>
```

Takes an audio file in WAV format and generates an image named `<input_wav_file>_spectrogram.png`. Each column of the image represents the result of the Fast Fourier Transform (FFT) of a single block from the audio file.
Height of the spectrogram image will be equal to `block_size / 2` and width will be equal to `floor(file_length / block_size)`.

# Audio generation from spectrogram

Usage:
```
python spectrogram2audio.py <input_image>
```
Interprets an image as a spectrogram and generates an audio file from it by calculating the Inverse Fast Fourier Transform (IFFT) of each column of the image.


![trance4 wav_spectrogram](https://github.com/akpizutti/spectrogram/assets/91564888/3324c3b2-3668-4c41-ae81-468ff4ef36c1)
Shown above is the spectrogram generated from [this audio file](https://drive.google.com/file/d/1Q8v6mDBkJEoBS7pD9hH4t_C0DbhDrdve/view?usp=sharing) (music composed by myself).




# TODO

Phase problem: A spectrogram only contains information of intensity of the frequencies, and not phase. 
This creates two problems: 

Firstly, it is not possible to recover an audio file from its generated spectrogram. 

Secondly, if the phases of all frequencies are reset on every block, there will be a click on every block transition (as shown in image below), which results in a very unpleasant sound. Solution to this is WIP.

![image](https://github.com/akpizutti/spectrogram/assets/91564888/62c0eb2a-6a73-44ed-a9c6-6c04e48b4acc)
