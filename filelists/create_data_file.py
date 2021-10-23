import re

files_path = "files/"

""" Read phonemes """
f = open(files_path + 'phoneme_transcriptions.txt', 'r')
lines = f.readlines()

# chars = set()

""" spliting test, train anf validation data """
test_lines = lines[:2800]
val_lines = lines[:int(len(lines)/10)]
train_lines = lines[int(len(lines)/10):]

def data_to_dict(line):
    data_lines_with_pitch = []
    data_lines_without_pitch = []
    for line in line:
        line = line.replace('\n', '')
        phoneme = line.split('\t')[1]
        name = line.split('\t')[0]

        phoneme = phoneme.replace('CH', 'c').replace('KH', 'k').replace('SH', 's').replace('SIL', 'i').replace('AH', 'h').replace('ZH', 'z').replace('AA', 'a')  ## replace multi chars by one new char
        phoneme = re.sub("\[([0-9]+)\]\s*", '', phoneme)

        """ One data is for preparing pith in model and another is for training dataa """
        data_line1 = name + ".wav|" + 'pitch/' + name + '.pt|' + phoneme
        data_line2 = name + ".wav|" + phoneme
        data_lines_with_pitch.append(data_line1)
        data_lines_without_pitch.append(data_line2)

    return data_lines_with_pitch, data_lines_without_pitch

train_data_with_pitch, train_data_without_pitch = data_to_dict(train_lines)
test_data_with_pitch, test_data_without_pitch = data_to_dict(test_lines)
val_data_with_pitch, val_data_without_pitch = data_to_dict(val_lines)

with open('audio_text_train.txt', 'w') as fp:
    for line in train_data_without_pitch:
        fp.write(line + '\n')
with open('audio_text_test.txt', 'w') as fp:
    for line in test_data_without_pitch:
        fp.write(line + '\n')
with open('audio_text_val.txt', 'w') as fp:
    for line in val_data_without_pitch:
        fp.write(line + '\n')

with open('audio_pitch_text_train.txt', 'w') as fp:
    for line in train_data_with_pitch:
        fp.write(line + '\n')
with open('audio_pitch_text_test.txt', 'w') as fp:
    for line in test_data_with_pitch:
        fp.write(line + '\n')
with open('audio_pitch_text_val.txt', 'w') as fp:
    for line in val_data_with_pitch:
        fp.write(line + '\n')
