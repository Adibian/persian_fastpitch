# Persian FastPitch
Training FastPitch for Persian language as a Persian text-to-speech. FastPitch is a TTS model that generates mel-spectrograms from text and is newer and faster than Tacotron.
In this implementation we use [FastPitch from Nvidia](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/SpeechSynthesis/FastPitch) and change it to train this model for persian language. We clone Nvidia-FastPitch and install its requirements and then do following changes:
1. Prepare persian data: many audio files and phonemes sequence for each file (we use phoneme instead of text because of using english characters and solving the problem of not writing some vowels in the Persian text)
2. Edit fastpitch/data_function.py beacause of erroe in google colab. You can see [this issue](https://github.com/NVIDIA/DeepLearningExamples/issues/1016)
3. Edit cleaners.py in common/text/ according to used characters in phonemes
4. Edit script/train.sh and train.py to change training parameters
5. Edit scripts/inference_example.sh to change inferencing parameter

## How to use
To use this implementation:
1. Clone this repository
2. Install requirements in requirments.txt 
3. Add your data: audio files to wavs/ and training and validating phoneme_transcriptions to filelists/ and testing phoneme_transcriptions to phrases/ as it is right now
4. Run following command to extract pitch from your audio files and save files to wavs/pitch/:
```
python prepare_dataset.py \
     --wav-text-filelists filelists/audio_text_train.txt \
                          filelists/audio_text_val.txt \
     --n-workers 16 \
     --batch-size 1 \
     --dataset-path 'wavs/' \
     --extract-pitch \
     --f0-method pyin
```
5. Run following command to install some dependencies:
```
git clone https://github.com/NVIDIA/apex
cd apex; pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
bash scripts/download_cmudict.sh
```
6. Train the model on your data using following command. The checkpoints file will be in output/
```
bash scripts/train.sh
```
7. Download WaveGlow to get audio from mel-spectrogram:
```
bash scripts/download_waveglow.sh
```
8. Run following command to get result of test file that you put in phrase/ in step 3. The synthesized audio will be in output/audio_test_file/:
```
bash scripts/inference_example.sh
```
