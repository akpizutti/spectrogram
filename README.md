# What it is
Two python scripts: one to generate a spectrogram from an audio file, and another to generate an audio file from an image interpreted as a spectrogram.

# Spectrogram generation
Usage:
```
python spectrogram.py <input_wav_file>
```

Takes an audio file in WAV format and generates an image named `<input_wav_file>_spectrogram.png`. Each column of the image represents the result of an FFT of a single block from the audio file.
Height of the spectrogram image will be equal to `block_size / 2` and width will be equal to `floor(file_length / block_size)`.

# Audio generation from spectrogram

TBA
