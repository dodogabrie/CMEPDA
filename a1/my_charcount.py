import os                                       # Manipulate path of my PC
import argparse                                 # Make --help description
import logging                                  # Make Debug and Warning 
import time                                     # Misure time of process
import math
import matplotlib.pyplot as plt                # for the istogram
import numpy as np
logging.basicConfig(level=logging.INFO)         # Definisce il livello di log


_description = 'Measure the releative frequencies of letters in a text file'


def print_res(ch,freq_dict,istogram):
    i = 0
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vec=np.zeros(len(freq_dict.values()))
    # Stampa le percentuali, un istogramma ascii e scrive dentro a vec i valori percentuali
    for ch, freq in freq_dict.items():
        letters[i]=ch
        vec[i]=freq*100.
        i+=1
        if freq*100. < 10:
            print('{}: {:.3f}% '.format(ch, freq*100. ), '#'*math.ceil( freq*100. - 0.5 ))
        else:
            print('{}: {:.3f}%'.format(ch, freq*100. ), '#'*math.ceil( freq*100. - 0.5 ))
    if istogram == 'y':
        # stampa l'istogramma su volontà dell'utente.
        plt.bar(letters, height=vec)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('My Very Own Histogram')
        maxfreq = vec.max()
        plt.ylim(ymax=maxfreq+1)
        plt.show()

def process(file_path,istogram):
    start = time.time()                         # Star measuring time
    """Main processing method.
    """
    # Basic sanity check: make sure that the file_argument points to an
    # existing text file.
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    # Open the input file (note that we are taking advantage of context
    # management, using a with statement).
    logging.info('Opening input file "%s"', file_path)
    with open(file_path) as input_file:             # Apre e chiude file  
        data = input_file.read()
    logging.info('Done. %d character(s) found.', len(data))
    # Prepare a dictionary to hold the letter frequencies, and initialize
    # all the counts to zero.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    freq_dict = {}                              # Tabella Hash
    for ch in letters:                          # Inizializzo a zero tutto
        freq_dict[ch] = 0

    # Loop over the input data (note the call to the lower() string method
    # that is casting everything in lower case).
    for ch in data.lower():                     # Lower mette tutto minuscolo
        if ch in letters:
            freq_dict[ch] += 1

    # One last loop over the letters to normalize the occurrences to 1.
    num_chars = float(sum(freq_dict.values()))
    for ch in letters:
        freq_dict[ch] /= num_chars

    # We're done---print the glorious output. (And here it is appropriate to
    # use print() instead of logging.)
    end = time.time()                           # Stop measuring time
    print_res(ch, freq_dict,istogram)        # Print Result with ascii istogram
    print('Elapsed time: %f' % (end-start))     # Print the elapsed time


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input file')
    parser.add_argument('istogram', help='adding mathplot istogram [y/n]')
    args = parser.parse_args()
    process(args.infile,args.istogram)
