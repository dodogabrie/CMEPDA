import os                                       # Manipulate path of my PC
import argparse                                 # Make --help description
import logging                                  # Make Debug and Warning 
import time                                     # Misure time of process
import math
import matplotlib.pyplot as plt                # for the istogram
import numpy as np
logging.basicConfig(level=logging.INFO)         # Definisce il livello di log


_description = 'Measure the releative frequencies of letters in a text file'


def istogram(yn,freq_dict):
    if yn == 'y':                               # Evito di eseguire se non serve
        letters = []                            # Inizializzo vuoti, riempio nel
        vec = []                                #   loop scorrendo il dizionario

        # Riempie i miei vettori per il plot scorrendo il dizionario.
        for ch, freq in freq_dict.items():
            letters.append(ch)
            vec = np.append(vec,freq*100)

        # stampa l'istogramma su volontà dell'utente.
        plt.bar(letters, height=vec)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Letters Frequencies')
        maxfreq = vec.max()
        plt.ylim(ymax=maxfreq+1)
        plt.show()
    else:
        return


def print_res(freq_dict):
    # Stampa le percentuali, un istogramma ascii e scrive dentro a vec i valori percentuali
    for ch, freq in freq_dict.items():
        if freq*100. < 10:
            #   lettera: perc                   esempio: 5% = #####, la funzione ceil arrotonda.
            print('{}: {:.3f}% '.format(ch, freq*100.), '#'*math.ceil( freq*100. - 0.5 ))
        else:
            print('{}: {:.3f}%'.format(ch, freq*100.), '#'*math.ceil( freq*100. - 0.5 ))

def process(file_path,inst):
    start = time.time()                         # Start measuring time
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
    print_res(freq_dict)                        # Print Result with ascii istogram
    end = time.time()                           # Stop measuring time
    istogram(inst,freq_dict)                      # Print Instrogram from matplotlib
    logging.info('Elapsed Time: %f sec', end-start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input file')
    parser.add_argument('--inst', type=str , default='n', help='add matplot istogram [y/n]')
    args = parser.parse_args()
    process(args.infile,args.inst)
