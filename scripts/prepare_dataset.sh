#!/usr/bin/env bash

set -e

python prepare_dataset.py \
     --wav-text-filelists filelists/audio_text_train.txt \
                          filelists/audio_text_val.txt \
     --n-workers 16 \
     --batch-size 1 \
     --dataset-path 'wavs/' \
     --extract-pitch \
     --f0-method pyin
