import logging                                  # Make Debug and Warning 
import matplotlib.pyplot as plt                # for the istogram
import numpy as np
import math

def print_stats(freq_dict,stats):
    if stats == 'y':
        print('tomorrow')


def extract(file_path,skip):
    """ Extract the text from .txt file.
    """
    start_string = '*** START OF THIS PROJECT GUTENBERG EBOOK CHIMERA WORLD ***'
    end_string = '*** END OF THIS PROJECT GUTENBERG EBOOK CHIMERA WORLD ***'
    logging.info('Opening input file "%s"', file_path)
    with open(file_path) as input_file:             # Apre e chiude file  
        data = input_file.read()
        len_data = len(data)
        if skip == 'y':                         # Estraggo i caratteri che mi servono.
            start = data.find(start_string) + len(start_string)
            stop = data.find(end_string)
            data = data[start:stop]
    logging.info('Done. %d character(s) found.', len_data)
    if skip == 'y':
        logging.info('Extract a book of %d character(s).', len(data))
    return data

def istogram(yn,freq_dict):
    """ Print ascii istogram.
    """
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


def print_freq(freq_dict):
    """ Print data and ascii istogram.
    """
    for ch, freq in freq_dict.items():
        if freq*100. < 10:
            #   lettera: perc                   esempio: 5% = #####, la funzione ceil arrotonda.
            print('{}: {:.3f}% '.format(ch, freq*100.), '#'*math.ceil( freq*100. - 0.5 ))
        else:
            print('{}: {:.3f}%'.format(ch, freq*100.), '#'*math.ceil( freq*100. - 0.5 ))


