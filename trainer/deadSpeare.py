from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from tensorflow.python.lib.io import file_io


import numpy as np
import pandas as pd
import argparse
from datetime import datetime
import time
# text=(open("/Users/pranjal/Desktop/text_generator/sonnets.txt").read())
#gs://deadspeare
def train_model(train_file='gs://deadspeare/deadpoolLines.txt', job_dir='./tmp/deadspeare', **args):
    logs_path = job_dir + '/logs/' + datetime.now().isoformat()
    print('-----------------------')
    print('Using train_file located at {}'.format(train_file))
    print('Using logs_path located at {}'.format(logs_path))
    print('-----------------------')
    file_stream = file_io.FileIO(train_file, mode='r')

    #Change this line to reading it via tensorflow library or something
    text=file_stream.read()
    # text=(open("sonnets.txt").read())

    text=text.lower()

    characters = sorted(list(set(text)))
    n_to_char = {n:char for n, char in enumerate(characters)}
    char_to_n = {char:n for n, char in enumerate(characters)}

    X = []
    Y = []
    length = len(text)
    seq_length = 100
    for i in range(0, length-seq_length, 1):
        sequence = text[i:i + seq_length]
        label =text[i + seq_length]
        X.append([char_to_n[char] for char in sequence])
        Y.append(char_to_n[label])

    X_modified = np.reshape(X, (len(X), seq_length, 1))
    X_modified = X_modified / float(len(characters))
    Y_modified = np_utils.to_categorical(Y)

    model = Sequential()
    model.add(LSTM(700, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(700, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(700))
    model.add(Dropout(0.2))
    model.add(Dense(Y_modified.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    #make batch size bigger
    model.fit(X_modified, Y_modified, epochs=100, batch_size=50)

    model.save_weights('deadpool_text_generator_gigantic_weights.h5')
    model.save('deadpool_text_generator_gigantic_fullmodel.h5')
    return model


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument(
      '--train-file',
      help='GCS or local paths to training data',
      required=True
    )
    parser.add_argument(
      '--job-dir',
      help='GCS location to write checkpoints and export models',
      required=True
    )
    args = parser.parse_args()
    arguments = args.__dict__

    model = train_model(**arguments)


    string_mapped = X[99]
    print("X[0,1,99] are: \n")
    print(X[0])
    print(X[1])
    print(X[99])
    full_string = [n_to_char[value] for value in string_mapped]
    # generating characters
    for i in range(seq_length):
        x = np.reshape(string_mapped,(1,len(string_mapped), 1))
        x = x / float(len(characters))
        pred_index = np.argmax(model.predict(x, verbose=0))
        seq = [n_to_char[value] for value in string_mapped]
        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]

    txt=""
    for char in full_string:
        txt = txt+char
    print(txt)
