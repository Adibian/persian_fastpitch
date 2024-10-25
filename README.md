# Persian FastPitch

**Persian FastPitch** is a fast and efficient TTS model adapted to generate mel-spectrograms from Persian text, using the **FastPitch** architecture. FastPitch, originally developed by NVIDIA, offers a significant speed advantage over Tacotron-based models by directly predicting pitch and leveraging parallelized training.

This implementation is based on [NVIDIA's FastPitch repository](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/SpeechSynthesis/FastPitch), adapted for Persian TTS. Changes made include language-specific adjustments and customizations to handle the unique aspects of Persian phonetics.

## Key Modifications

1. **Prepare Persian Data**: Collect Persian audio files and generate corresponding phoneme sequences for each. This uses phonemes instead of text for better accuracy, handling challenges like missing vowels in Persian script.
2. **Resolve Colab Error in `data_function.py`**: Minor edits to address Colab compatibility issues. See [issue #1016](https://github.com/NVIDIA/DeepLearningExamples/issues/1016) for more details.
3. **Update `cleaners.py` in `common/text/`**: Adapt character handling to Persian phonemes.
4. **Customize Training Parameters**: Modify `scripts/train.sh` and `train.py` to fit Persian data.
5. **Adjust Inference Parameters**: Update `scripts/inference_example.sh` for Persian-specific inference.

---

## How to Use

1. **Clone this Repository**
   ```bash
   git clone https://github.com/Adibian/Persian-FastPitch.git
   cd Persian-FastPitch
   
2. **Install Requirements**
   ```bash
   pip install -r requirements.txt

3. **Add Your Data**
     * Place audio files in wavs/
     * Add training and validation phoneme transcriptions to filelists/
     * Add test phoneme transcriptions to phrases/
   
4. **Extract Pitch**
     * Run this command to extract pitch values for the audio files
        ```bash
          python prepare_dataset.py \
              --wav-text-filelists filelists/audio_text_train.txt \
                                   filelists/audio_text_val.txt \
              --n-workers 16 \
              --batch-size 1 \
              --dataset-path 'wavs/' \
              --extract-pitch \
              --f0-method pyin
5. **Install Additional Dependencies**
     * Run the following to install NVIDIA Apex and download CMUdict:
       ```bash
          git clone https://github.com/NVIDIA/apex
          cd apex; pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
          bash scripts/download_cmudict.sh
       
6. **Train the Model**
     * Use this command to start training. Checkpoints will be saved in output/:
     ```bash
     bash scripts/train.sh
     
7. **Download WaveGlow Vocoder**
     * WaveGlow is required to convert mel-spectrograms into audio. Download it using:
       ```bash
       bash scripts/download_waveglow.sh
       
7. **Run Inference**
     * To synthesize audio for a test file in phrases/, run:
       ```bash
       bash scripts/inference_example.sh
     * The synthesized audio will be saved in output/audio_test_file/.
